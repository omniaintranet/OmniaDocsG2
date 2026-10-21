#!/usr/bin/env python3
"""Rule-based review of documentation changes (see .github/docs-review/README.md).

Modes:
  --base REF        review what the working tree changes compared with REF (pull requests)
  --all             review every page on the current checkout (baseline)
  --files F [F ...] review the given files completely (test fixtures)

Writes findings.json and summary.md to --out, prints GitHub annotations with
--annotations, and exits with 1 when an error-level finding is reported.
"""

from __future__ import annotations

import argparse
import collections
import dataclasses
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
CONFIG_DIR = ROOT / ".github" / "docs-review"
VALE_CONFIG = CONFIG_DIR / "vale" / ".vale.ini"
VALE_STYLE = CONFIG_DIR / "vale" / "styles" / "Omnia"
GITLEAKS_CONFIG = CONFIG_DIR / "gitleaks.toml"
README_PATH = ".github/docs-review/README.md"
COMMENT_MARKER = "<!-- docs-review-summary -->"

SEVERITIES = ("error", "warning", "info")
AREAS = {
    "Omnia": "Audience and tone",
    "Confidential": "Confidentiality",
    "Reference": "Confidentiality",
    "Secrets": "Confidentiality",
    "Structure": "Structure",
    "Build": "Structure",
    "Links": "Structure",
}


@dataclasses.dataclass
class Finding:
    rule: str
    severity: str
    file: str
    line: int | None
    message: str

    @property
    def area(self) -> str:
        return AREAS.get(self.rule.split(".", 1)[0], "Other")


# ---------------------------------------------------------------- helpers


def run(cmd: list[str], cwd: Path = ROOT, check: bool = True, env: dict | None = None) -> str:
    result = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and result.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:4])} ... failed ({result.returncode}):\n{result.stderr[-2000:]}")
    return result.stdout


def git(*args: str) -> str:
    return run(["git", *args])


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def glob_to_regex(pattern: str) -> re.Pattern:
    out = ""
    i = 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out += "(?:.*/)?"
            i += 3
        elif pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif pattern[i] == "*":
            out += "[^/]*"
            i += 1
        elif pattern[i] == "?":
            out += "[^/]"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile(out + r"\Z")


def matches_any(path: str, patterns: list[str]) -> bool:
    return any(glob_to_regex(p).match(path) for p in patterns)


def find_tool(name: str, env_var: str) -> str | None:
    return os.environ.get(env_var) or shutil.which(name)


# ---------------------------------------------------------------- config


class Config:
    def __init__(self) -> None:
        self.settings = load_yaml(CONFIG_DIR / "settings.yml")
        self.confidential = load_yaml(CONFIG_DIR / "confidentiality.yml")
        self.exclude = self.settings.get("exclude", [])
        self.draft_markers = [re.compile(p, re.M) for p in self.settings.get("drafts", {}).get("markers", [])]
        words = self.settings.get("draft_note_words", [])
        self.draft_note = re.compile(r"^(?:%s)\b" % "|".join(re.escape(w) for w in words)) if words else None
        self.suppress = self.settings.get("suppress", [])
        self.image_ext = tuple("." + e.lower() for e in self.settings.get("images", {}).get("extensions", []))
        self.patterns = []
        for p in self.confidential.get("patterns", []):
            allow = [re.compile(a, re.I) for a in p.get("allow", [])]
            self.patterns.append((p["id"], p["severity"], p["message"], re.compile(p["regex"], re.I), allow))
        self.refs = self.confidential.get("customer_references")
        if self.refs:
            self.refs_regex = re.compile(self.refs["regex"])
        internal = load_yaml(VALE_STYLE / "InternalLanguage.yml")
        self.internal_message = internal["message"]
        self.internal_regex = re.compile(r"\b(?:%s)\b" % "|".join(internal["tokens"]), re.I)

    def is_doc(self, path: str) -> bool:
        return path.endswith(".rst") and not matches_any(path, self.exclude)

    def is_image(self, path: str) -> bool:
        return path.lower().endswith(self.image_ext) and not matches_any(path, self.exclude)

    def suppressed_by_settings(self, rule: str, path: str) -> bool:
        for entry in self.suppress:
            rule_re = glob_to_regex(entry.get("rule", "*").replace(".", "/"))
            if rule_re.match(rule.replace(".", "/")) and matches_any(path, entry.get("files", ["**"])):
                return True
        return False


# ---------------------------------------------------------------- rst parsing

DIRECTIVE = re.compile(r"^(\s*)\.\.\s+(?:\|[^|]+\|\s+)?([\w:.+-]+)::(.*)$")
NOT_COMMENT = re.compile(r"^\s*\.\.\s+(?:[\w:.+-]+::|_|\||\[)")
COMMENT = re.compile(r"^(\s*)\.\.(?:\s+(.*))?$")
VALE_SWITCH = re.compile(r"^\s*\.\.\s+vale\s+(on|off)\s*$", re.I)
VALE_RULE = re.compile(r"^\s*\.\.\s+vale\s+([\w.]+)\s*=\s*(YES|NO)\s*$", re.I)
ADORNMENT = re.compile(r"^([!-/:-@\[-`{-~])\1{2,}\s*$")
LITERAL_DIRECTIVES = {"code-block", "code", "sourcecode", "raw", "literalinclude", "parsed-literal"}


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip())


class RstFile:
    def __init__(self, path: str, text: str, config: Config) -> None:
        self.path = path
        self.lines = text.splitlines()
        self.config = config
        self.comment_blocks: list[tuple[int, int, str]] = []  # (first line, last line, first text)
        self.comment_lines: set[int] = set()
        self.literal_lines: set[int] = set()
        self.off_all: dict[int, bool] = {}
        self.off_rules: dict[int, frozenset] = {}
        self.is_draft = any(m.search("\n".join(self.lines[:15])) for m in config.draft_markers)
        self._scan()

    def _block_end(self, start: int, base_indent: int) -> int:
        """Last line (0-based) of the indented block that follows line `start`."""
        end = start
        j = start + 1
        while j < len(self.lines):
            line = self.lines[j]
            if line.strip() and indent_of(line) <= base_indent:
                break
            if line.strip():
                end = j
            j += 1
        return end

    def _scan(self) -> None:
        off_all = False
        off_rules: set[str] = set()
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            switch = VALE_SWITCH.match(line)
            rule = VALE_RULE.match(line)
            if switch:
                off_all = switch.group(1).lower() == "off"
            elif rule:
                (off_rules.add if rule.group(2).upper() == "NO" else off_rules.discard)(rule.group(1))
            self.off_all[i + 1] = off_all
            self.off_rules[i + 1] = frozenset(off_rules)
            i += 1

        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            comment = COMMENT.match(line)
            directive = DIRECTIVE.match(line)
            if comment and not NOT_COMMENT.match(line):
                end = self._block_end(i, indent_of(line))
                first = (comment.group(2) or "").strip()
                if not first and end > i:
                    first = self.lines[i + 1].strip()
                self.comment_blocks.append((i + 1, end + 1, first))
                self.comment_lines.update(range(i + 1, end + 2))
                i = end + 1
                continue
            literal = False
            if directive:
                literal = directive.group(2) in LITERAL_DIRECTIVES
            elif line.rstrip().endswith("::") and not line.strip().startswith(".."):
                literal = True
            if literal:
                end = self._block_end(i, indent_of(line))
                self.literal_lines.update(range(i + 2, end + 2))
                i = end + 1
                continue
            i += 1

    def suppressed(self, rule: str, line: int | None) -> bool:
        if line and (self.off_all.get(line) or rule in self.off_rules.get(line, ())):
            return True
        return self.config.suppressed_by_settings(rule, self.path)

    def headings(self) -> list[tuple[int, str, tuple[str, str]]]:
        """(line, title, style) for every section title, in order."""
        result = []
        lines = self.lines
        i = 0
        while i < len(lines) - 1:
            line = lines[i]
            over = ADORNMENT.match(line)
            if over and i + 2 < len(lines) and lines[i + 1].strip() and ADORNMENT.match(lines[i + 2]) \
                    and lines[i + 2][0] == line[0] and (i == 0 or not lines[i - 1].strip()):
                result.append((i + 2, lines[i + 1].strip(), ("over", line[0])))
                i += 3
                continue
            under = ADORNMENT.match(lines[i + 1])
            if under and line.strip() and not line[0].isspace() and not ADORNMENT.match(line) \
                    and not line.startswith("..") and (i == 0 or not lines[i - 1].strip()) \
                    and (i + 1 not in self.comment_lines):
                result.append((i + 1, line.strip(), ("under", lines[i + 1][0])))
                i += 2
                continue
            i += 1
        return result

    def images(self):
        """(line, target, option lines, has alt) for every image and figure directive."""
        for i, line in enumerate(self.lines):
            directive = DIRECTIVE.match(line)
            if not directive or directive.group(2) not in ("image", "figure"):
                continue
            end = self._block_end(i, indent_of(line))
            options = [j + 1 for j in range(i + 1, end + 1) if self.lines[j].strip().startswith(":")]
            has_alt = any(self.lines[j - 1].strip().startswith(":alt:") for j in options)
            yield i + 1, directive.group(3).strip(), options, has_alt


def style_label(style: tuple[str, str]) -> str:
    kind, char = style
    return f"'{char * 5}' above and below" if kind == "over" else f"'{char * 5}' underline"


# ---------------------------------------------------------------- checks


class Review:
    def __init__(self, config: Config, changed: dict[str, set[int] | None]) -> None:
        self.config = config
        self.changed = changed  # path -> changed line numbers, None = every line
        self.findings: list[Finding] = []
        self.notes: list[str] = []
        self.images_to_check: list[str] = []
        self.files: dict[str, RstFile] = {}
        for path in changed:
            full = ROOT / path if not Path(path).is_absolute() else Path(path)
            if full.exists():
                self.files[path] = RstFile(path, full.read_text(encoding="utf-8", errors="replace"), config)

    def in_scope(self, path: str, line: int | None) -> bool:
        lines = self.changed.get(path, set())
        return lines is None or line is None or line in lines

    def add(self, rule: str, severity: str, path: str, line: int | None, message: str) -> None:
        rst = self.files.get(path)
        if rst is not None and rst.suppressed(rule, line):
            return
        if rst is None and self.config.suppressed_by_settings(rule, path):
            return
        self.findings.append(Finding(rule, severity, path, line, message))

    # -- Python rules on the raw source

    def check_source(self) -> None:
        for path, rst in self.files.items():
            for number, text in enumerate(rst.lines, 1):
                if not self.in_scope(path, number):
                    continue
                self._check_patterns(path, number, text)
                if number not in rst.comment_lines and number not in rst.literal_lines:
                    self._check_references(path, number, text)
            self._check_comments(path, rst)
            self._check_headings(path, rst)
            self._check_image_alt(path, rst)

    def _check_patterns(self, path: str, number: int, text: str) -> None:
        reported: list[tuple[int, int]] = []
        for rule, severity, message, regex, allow in self.config.patterns:
            for match in regex.finditer(text):
                found = match.group(0)
                if any(a.fullmatch(found) for a in allow):
                    continue
                if any(start <= match.start() and match.end() <= end for start, end in reported):
                    continue  # already reported by an earlier pattern
                reported.append(match.span())
                self.add(rule, severity, path, number, f"`{found}`: {message}")

    def _check_references(self, path: str, number: int, text: str) -> None:
        refs = self.config.refs
        if not refs:
            return
        for match in self.config.refs_regex.finditer(text):
            value = int(match.group(1))
            if value < refs["min_customer_reference"]:
                self.add(refs["error_id"], "error", path, number, refs["error_message"].format(number=value))
            else:
                self.add(refs["info_id"], "info", path, number, refs["info_message"].format(number=value))

    def _check_comments(self, path: str, rst: RstFile) -> None:
        for first, last, first_text in rst.comment_blocks:
            if VALE_SWITCH.match(rst.lines[first - 1]) or VALE_RULE.match(rst.lines[first - 1]):
                continue
            for number in range(first, last + 1):
                if not self.in_scope(path, number):
                    continue
                for match in self.config.internal_regex.finditer(rst.lines[number - 1]):
                    message = self.config.internal_message.replace("%s", match.group(0))
                    self.add("Omnia.InternalLanguage", "warning", path, number,
                             message + " (In an rst comment: not shown on the site, but anyone can read it in this public repository.)")
            note = self.config.draft_note
            if note and not rst.is_draft and note.match(first_text) and self.in_scope(path, first):
                self.add("Omnia.DraftNote", "info", path, first,
                         "Draft note in an rst comment. It is not shown on the site; remove it when the page is final.")

    def _check_headings(self, path: str, rst: RstFile) -> None:
        styles: list[tuple[str, str]] = []
        level = 0
        for number, title, style in rst.headings():
            if style in styles:
                new_level = styles.index(style) + 1
                jump = new_level > level + 1
            else:
                jump = len(styles) != level
                new_level = len(styles) + 1
                if not jump:
                    styles.append(style)
            if jump and self.in_scope(path, number):
                expected = style_label(styles[level]) if level < len(styles) else "a new heading style"
                self.add("Structure.HeadingLevel", "warning", path, number,
                         f"Heading '{title}' skips a level after a level {level} heading. "
                         f"Use {expected} for a level {level + 1} heading. Sphinx drops or misplaces such sections.")
                continue
            level = new_level

    def _check_image_alt(self, path: str, rst: RstFile) -> None:
        for number, target, options, has_alt in rst.images():
            if has_alt or not any(self.in_scope(path, n) for n in [number, *options]):
                continue
            self.add("Structure.ImageAlt", "warning", path, number,
                     f"Image `{target}` has no `:alt:` text. Add a short description for screen readers.")

    # -- images

    def check_images(self, changed_images: dict[str, str], all_docs: list[str]) -> None:
        if not changed_images:
            return
        referenced: set[str] = set()
        for doc in all_docs:
            rst = RstFile(doc, (ROOT / doc).read_text(encoding="utf-8", errors="replace"), self.config)
            base = Path(doc).parent
            for _, target, _, _ in rst.images():
                if "://" in target:
                    continue
                resolved = Path(target.lstrip("/")) if target.startswith("/") else base / target
                referenced.add(os.path.normpath(resolved).replace("\\", "/"))
            for match in re.finditer(r":download:`(?:[^<`]*<)?([^>`]+)>?`", "\n".join(rst.lines)):
                referenced.add(os.path.normpath(base / match.group(1)).replace("\\", "/"))
        for path, status in sorted(changed_images.items()):
            self.images_to_check.append(path)
            if status in ("A", "R") and path not in referenced:
                self.add("Structure.UnusedImage", "warning", path, None,
                         "Image file is not used on any page. Reference it with `.. image::` or remove it.")

    # -- Vale

    def check_vale(self, paths: list[str]) -> None:
        if not paths:
            return
        vale = find_tool("vale", "VALE_BIN")
        if not vale:
            raise RuntimeError("Vale is not installed. Install it or set VALE_BIN (see README.md).")
        env = dict(os.environ)
        env["PATH"] = str(Path(sys.executable).parent) + os.pathsep + env.get("PATH", "")
        levels = {"error": "error", "warning": "warning", "suggestion": "info"}
        for start in range(0, len(paths), 100):
            chunk = paths[start:start + 100]
            out = run([vale, "--config", str(VALE_CONFIG), "--output", "JSON", "--no-exit", *chunk], env=env, check=False)
            try:
                alerts = json.loads(out or "{}")
            except json.JSONDecodeError as error:
                raise RuntimeError(f"Vale returned no JSON: {out[:500]}") from error
            if "Code" in alerts and "Text" in alerts:
                raise RuntimeError(f"Vale failed: {alerts['Text']}")
            by_name = {os.path.normcase(os.path.abspath(ROOT / p)): p for p in chunk}
            for name, items in alerts.items():
                path = by_name.get(os.path.normcase(os.path.abspath(ROOT / name)), name.replace("\\", "/"))
                for alert in items:
                    line = alert["Line"]
                    if self.in_scope(path, line):
                        self.add(alert["Check"], levels.get(alert["Severity"], "info"), path, line, alert["Message"])

    # -- gitleaks

    def check_secrets(self, base: str | None, paths: list[str]) -> None:
        gitleaks = find_tool("gitleaks", "GITLEAKS_BIN")
        if not gitleaks:
            raise RuntimeError("gitleaks is not installed. Install it or set GITLEAKS_BIN (see README.md).")
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "gitleaks.json"
            common = ["--config", str(GITLEAKS_CONFIG), "--report-format", "json", "--report-path", str(report),
                      "--exit-code", "0", "--no-banner", "--redact"]
            results = []
            if base:
                run([gitleaks, "git", "--log-opts", f"{base}..HEAD", *common, str(ROOT)])
                results = json.loads(report.read_text(encoding="utf-8") or "[]")
            else:
                for path in paths:
                    run([gitleaks, "dir", *common, str((ROOT / path).resolve())])
                    for item in json.loads(report.read_text(encoding="utf-8") or "[]"):
                        item["File"] = path
                        results.append(item)
        seen = set()
        for item in results:
            path = item["File"].replace("\\", "/")
            if Path(path).is_absolute():
                path = os.path.relpath(path, ROOT).replace("\\", "/")
            key = (item["RuleID"], path, item["StartLine"])
            if key in seen:
                continue
            seen.add(key)
            self.add(f"Secrets.{item['RuleID']}", "error", path, item["StartLine"],
                     f"Possible secret ({item['Description']}). Remove it and ask a developer to revoke it: "
                     "it stays in the Git history of this public repository.")

    # -- Sphinx build

    def check_build(self, base: str, renames: dict[str, str]) -> None:
        build = self.config.settings.get("build", {})
        ignore = [re.compile(p) for p in build.get("ignore", [])]
        options = build.get("options", [])
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            base_dir = tmp_path / "base"
            git("worktree", "add", "--detach", str(base_dir), base)
            try:
                base_warnings = sphinx_warnings(base_dir, tmp_path / "base-html", options, ignore)
            finally:
                git("worktree", "remove", "--force", str(base_dir))
            head_warnings = sphinx_warnings(ROOT, tmp_path / "head-html", options, ignore)
        base_count = collections.Counter(
            (renames.get(loc, loc), sev, msg) for loc, _, sev, msg in base_warnings)
        head_count = collections.Counter((loc, sev, msg) for loc, _, sev, msg in head_warnings)
        new = head_count - base_count
        fixed = base_count - head_count
        for loc, line, sev, msg in reversed(head_warnings):
            key = (loc, sev, msg)
            if new[key] <= 0:
                continue
            new[key] -= 1
            rule, text = classify_warning(msg)
            path = loc if loc and not loc.startswith("<") else "(Sphinx build)"
            self.add(rule, "error", path, line, f"{text} (Sphinx: {sev}: {msg.splitlines()[0]})")
        if fixed:
            self.notes.append(f"This pull request fixes {sum(fixed.values())} existing Sphinx build warning(s).")

    # -- links

    def check_links(self, docs: list[str]) -> None:
        settings = self.config.settings.get("linkcheck", {})
        if not docs or not settings.get("enabled", True):
            return
        ignore = [re.compile(p) for p in settings.get("ignore", [])]
        with tempfile.TemporaryDirectory() as tmp:
            # -D cannot set linkcheck_timeout (its default is None, so the value stays a string),
            # so a wrapper configuration runs the repository's conf.py and adds the link settings.
            conf_dir = Path(tmp) / "conf"
            conf_dir.mkdir()
            (conf_dir / "conf.py").write_text("\n".join([
                f"exec(compile(open({str(ROOT / 'conf.py')!r}, encoding='utf-8').read(), 'conf.py', 'exec'))",
                f"linkcheck_timeout = {int(settings.get('timeout', 20))}",
                f"linkcheck_retries = {int(settings.get('retries', 2))}",
                f"linkcheck_anchors = {bool(settings.get('check_anchors', False))}",
                ""]), encoding="utf-8")
            run([sys.executable, "-m", "sphinx", "-b", "linkcheck", "-q", "-N", "-j", "auto", "-c", str(conf_dir),
                 str(ROOT), str(Path(tmp) / "out"), *docs], check=False)
            output = Path(tmp) / "out" / "output.json"
            ran = output.exists()
            rows = [json.loads(l) for l in output.read_text(encoding="utf-8").splitlines() if l.strip()] if ran else []
        if not ran:
            self.notes.append("The external link check did not run (no result from Sphinx linkcheck).")
        for row in rows:
            path = row["filename"].replace("\\", "/")
            if row["status"] not in ("broken", "timeout") or path not in docs:
                continue
            if any(p.search(row["uri"]) for p in ignore) or not self.in_scope(path, row.get("lineno")):
                continue
            reason = "timed out" if row["status"] == "timeout" else (row.get("info") or "broken")
            self.add("Links.Broken", "warning", path, row.get("lineno"),
                     f"Link does not work: {row['uri']} ({str(reason)[:150]})")


ANSI = re.compile(r"\x1b\[[0-9;]*m")
WARNING_LINE = re.compile(r"^(?:(?P<loc>.*?)(?::(?P<line>\d+))?: )?(?P<sev>WARNING|ERROR|SEVERE|CRITICAL): (?P<msg>.*)$")


def sphinx_warnings(src: Path, out: Path, options: list[str], ignore: list[re.Pattern]):
    warn_file = out.parent / (out.name + "-warnings.txt")
    result = subprocess.run([sys.executable, "-m", "sphinx", "-b", "html", "-q", "-N", "-j", "auto", *options,
                             "-w", str(warn_file), str(src), str(out)],
                            cwd=src, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        raise RuntimeError(f"Sphinx build of {src} failed:\n{result.stderr[-3000:]}")
    prefixes = {str(src) + os.sep, str(src).replace("\\", "/") + "/", str(src.resolve()) + os.sep}
    records: list[list] = []
    text = ANSI.sub("", warn_file.read_text(encoding="utf-8", errors="replace"))
    for raw in text.splitlines():
        match = WARNING_LINE.match(raw)
        if match:
            records.append([match.group("loc") or "", int(match.group("line")) if match.group("line") else None,
                            match.group("sev"), match.group("msg")])
        elif records:
            records[-1][3] += "\n" + raw
    result_records = []
    for loc, line, sev, msg in records:
        for prefix in prefixes:
            loc = loc.replace(prefix, "")
            msg = msg.replace(prefix, "")
        loc = loc.replace("\\", "/")
        if any(p.search(f"{loc}: {msg}") for p in ignore):
            continue
        result_records.append((loc, line, sev, msg.strip()))
    return result_records


def classify_warning(message: str) -> tuple[str, str]:
    if "isn't included in any toctree" in message:
        return ("Build.NotInToctree",
                "This page is not in any table of contents (toctree), so readers cannot find it in the navigation. "
                "Add it to the toctree of its section's index.rst, or add `:orphan:` at the top if that is intended.")
    if re.search(r"unknown document|undefined label|Unknown target name|nonexisting document|duplicate label"
                 r"|reference target not found|Duplicate explicit target", message):
        return "Build.BrokenReference", "Broken internal link or reference."
    if "image file not readable" in message:
        return "Build.MissingImage", "Image file is missing."
    if "Title" in message and ("level" in message or "underline" in message or "overline" in message):
        return "Build.Heading", "Heading markup problem."
    return "Build.Warning", "New Sphinx build warning."


# ---------------------------------------------------------------- diff


def changed_lines(diff_base: str) -> dict[str, set[int]]:
    result: dict[str, set[int]] = {}
    current = None
    for line in git("diff", "-U0", "--find-renames", "--no-color", diff_base, "--").splitlines():
        if line.startswith("+++ "):
            current = None if line[4:] == "/dev/null" else line[6:]
            if current is not None:
                result.setdefault(current, set())
        elif line.startswith("@@") and current is not None:
            match = re.search(r"\+(\d+)(?:,(\d+))?", line)
            start, count = int(match.group(1)), int(match.group(2) or 1)
            result[current].update(range(start, start + count))
    return result


def changed_files(diff_base: str) -> tuple[dict[str, str], dict[str, str]]:
    """Path -> status letter (A, M, R, D...) and renames old -> new."""
    status: dict[str, str] = {}
    renames: dict[str, str] = {}
    for line in git("diff", "--name-status", "--find-renames", "--no-color", diff_base, "--").splitlines():
        parts = line.split("\t")
        letter = parts[0][0]
        if letter == "R":
            renames[parts[1]] = parts[2]
            status[parts[2]] = "R"
        else:
            status[parts[1]] = letter
    for path in git("ls-files", "--others", "--exclude-standard").splitlines():
        status[path] = "A"
    return status, renames


# ---------------------------------------------------------------- report


def sort_key(finding: Finding):
    return (SEVERITIES.index(finding.severity), finding.file, finding.line or 0, finding.rule)


def link_for(finding: Finding, link_base: str | None) -> str:
    where = finding.file + (f", line {finding.line}" if finding.line else "")
    if not link_base or finding.file.startswith("("):
        return where
    anchor = f"#L{finding.line}" if finding.line else ""
    return f"[{where}]({link_base}/{finding.file}{anchor})"


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def table(findings: list[Finding], link_base: str | None, limit: int = 60) -> list[str]:
    rows = ["| Where | What to do | Check |", "| --- | --- | --- |"]
    for finding in findings[:limit]:
        rows.append(f"| {cell(link_for(finding, link_base))} | {cell(finding.message)} | "
                    f"{finding.area}: `{finding.rule}` |")
    if len(findings) > limit:
        rows.append(f"| | ... and {len(findings) - limit} more: see the job log. | |")
    return rows


def summary(review: Review, scope: str, link_base: str | None, commit: str | None) -> str:
    by_severity = {s: [f for f in sorted(review.findings, key=sort_key) if f.severity == s] for s in SEVERITIES}
    errors, warnings, infos = by_severity["error"], by_severity["warning"], by_severity["info"]
    readme = f"{link_base}/{README_PATH}" if link_base else README_PATH
    lines = [COMMENT_MARKER]
    if errors:
        lines.append(f"## ❌ Documentation review: {len(errors)} problem(s) must be fixed before merging")
    else:
        lines.append("## ✅ Documentation review: nothing blocks this pull request")
    lines += ["", f"{scope} Checked: audience and tone, confidentiality, structure. "
                  f"[What each check does, and what to do about a false alarm]({readme}).", ""]
    if errors:
        lines += [f"### Must fix ({len(errors)})", "", *table(errors, link_base), ""]
    if warnings:
        lines += [f"### Please check ({len(warnings)}, does not block)", "", *table(warnings, link_base), ""]
    if infos:
        lines += [f"<details><summary>For information ({len(infos)})</summary>", "",
                  *table(infos, link_base), "", "</details>", ""]
    if review.images_to_check:
        lines += [f"### Images to look at ({len(review.images_to_check)})", "",
                  "These images were added or changed. Screenshots cannot be checked automatically: make sure they "
                  "show no customer names, real people, email addresses or tenant addresses.", ""]
        for path in review.images_to_check[:40]:
            lines.append(f"- [{path}]({link_base}/{path})" if link_base else f"- {path}")
        lines.append("")
    if not (errors or warnings or infos or review.images_to_check):
        lines += ["No findings.", ""]
    for note in review.notes:
        lines += [f"> {note}", ""]
    footer = "Errors block the check; warnings and information do not."
    if commit:
        footer = f"Updated for commit {commit[:7]}. " + footer
    lines.append(f"<sub>{footer}</sub>")
    return "\n".join(lines) + "\n"


def escape_data(text: str) -> str:
    return text.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def escape_property(text: str) -> str:
    return escape_data(text).replace(":", "%3A").replace(",", "%2C")


def print_annotations(findings: list[Finding]) -> None:
    kinds = {"error": "error", "warning": "warning", "info": "notice"}
    for finding in sorted(findings, key=sort_key):
        props = [f"title={escape_property(finding.rule)}"]
        if not finding.file.startswith("("):
            props.insert(0, f"file={escape_property(finding.file)}")
            if finding.line:
                props.insert(1, f"line={finding.line}")
        print(f"::{kinds[finding.severity]} {','.join(props)}::{escape_data(finding.message)}")


# ---------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--base", help="base branch or commit of the pull request")
    mode.add_argument("--all", action="store_true", help="review every page (baseline)")
    mode.add_argument("--files", nargs="+", help="review these files completely (fixtures)")
    parser.add_argument("--out", default="_build/docs-review", help="folder for findings.json and summary.md")
    parser.add_argument("--build", choices=["auto", "always", "never"], default="auto",
                        help="compare Sphinx builds of the base and the change (default: when pages changed)")
    parser.add_argument("--linkcheck", choices=["auto", "never"], default="auto")
    parser.add_argument("--no-secrets", action="store_true", help="skip gitleaks")
    parser.add_argument("--annotations", action="store_true", help="print GitHub annotations")
    parser.add_argument("--step-summary", action="store_true", help="add the summary to the GitHub job summary")
    parser.add_argument("--link-base", help="URL prefix for links to files, e.g. https://github.com/o/r/blob/<sha>")
    parser.add_argument("--commit", help="commit shown in the summary")
    parser.add_argument("--no-fail", action="store_true", help="exit 0 even when errors are found")
    args = parser.parse_args(argv)

    config = Config()
    status: dict[str, str] = {}
    renames: dict[str, str] = {}
    diff_base = None
    if args.base:
        diff_base = git("merge-base", args.base, "HEAD").strip()
        status, renames = changed_files(diff_base)
        lines = changed_lines(diff_base)
        changed: dict[str, set[int] | None] = {}
        for path, letter in status.items():
            if config.is_doc(path) and letter != "D":
                changed[path] = None if letter == "A" and path not in lines else lines.get(path, set())
        images = {p: s for p, s in status.items() if config.is_image(p) and s != "D"}
        scope = (f"{len(changed)} changed page(s) and {len(images)} image(s) in this pull request."
                 if changed or images else "This pull request changes no documentation pages or images.")
    elif args.all:
        tracked = git("ls-files").splitlines()
        changed = {p: None for p in tracked if config.is_doc(p)}
        images = {p: "A" for p in tracked if config.is_image(p)}
        scope = f"All {len(changed)} pages and {len(images)} images (baseline)."
    else:
        changed = {}
        for name in args.files:
            path = Path(name).resolve()
            try:
                changed[path.relative_to(ROOT).as_posix()] = None
            except ValueError:
                changed[str(path)] = None
        images = {}
        scope = f"{len(changed)} file(s)."

    review = Review(config, changed)
    review.check_source()
    review.check_vale(sorted(changed))
    all_docs = [p for p in git("ls-files").splitlines() if config.is_doc(p)] + \
        [p for p, s in status.items() if s == "A" and config.is_doc(p)]
    review.check_images(images, sorted(set(all_docs)))
    if not args.no_secrets:
        review.check_secrets(diff_base, sorted(changed) if not diff_base else [])
    if diff_base:
        relevant = [p for p in status if config.is_doc(p) or config.is_image(p)
                    or p in ("conf.py", "docs/requirements.txt") or p.startswith("_templates/")]
        if args.build == "always" or (args.build == "auto" and relevant):
            review.check_build(diff_base, renames)
        if args.linkcheck == "auto":
            review.check_links(sorted(p for p, l in changed.items() if l is None or l))

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "findings.json").write_text(json.dumps(
        [dataclasses.asdict(f) | {"area": f.area} for f in sorted(review.findings, key=sort_key)], indent=2),
        encoding="utf-8")
    text = summary(review, scope, args.link_base, args.commit)
    (out / "summary.md").write_text(text, encoding="utf-8")
    if args.step_summary and os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as handle:
            handle.write(text)
    if args.annotations:
        print_annotations(review.findings)

    counts = collections.Counter(f.severity for f in review.findings)
    print(f"Documentation review: {counts['error']} error(s), {counts['warning']} warning(s), "
          f"{counts['info']} info. Summary: {out / 'summary.md'}")
    return 1 if counts["error"] and not args.no_fail else 0


if __name__ == "__main__":
    sys.exit(main())
