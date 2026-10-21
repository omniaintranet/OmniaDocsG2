# Documentation review

Every pull request into `master` is checked by the workflow **Documentation review**
(`.github/workflows/docs-review.yml`) before the change is published.

- The result appears as **one comment** on the pull request. It is updated on every new push, so there is never more
  than one.
- The problems are also marked on the changed lines in the **Files changed** tab.
- **Must fix** (errors) makes the check fail. Fix them before merging.
- **Please check** (warnings) and **For information** do not block. Read them and decide.
- Only lines that the pull request adds or changes are reported. Existing text on `master` does not make a pull
  request fail.

GitHub Copilot can also review the wording of a pull request (see "Copilot review" below). It only comments and
never blocks.

## What is checked

| Area | Rule | What it finds | Result |
| --- | --- | --- | --- |
| Audience and tone | `Omnia.InternalLanguage` | Internal or sales language: "key selling point", "upsell", "competitive advantage", "USP", "win deals", ... | Must fix (in an rst comment: please check) |
| Audience and tone | `Omnia.Leftovers` | Unfinished text: TODO, TBD, FIXME, XXX, "lorem ipsum", "add screenshot", ... | Must fix |
| Audience and tone | `Omnia.Superlatives` | Marketing words: "best-in-class", "revolutionary", "game-changer", "world-class", ... | Please check |
| Audience and tone | `Omnia.FuturePromises` | Promises: "coming soon", "in a future release", "planned for", "will be available in 7.14", ... (not on roadmap pages) | Please check |
| Audience and tone | `Omnia.DraftNote` | Draft notes in rst comments (`.. REVIEW: ...`) on pages that are not drafts | For information |
| Confidentiality | `Confidential.Email` | Email addresses (except placeholders such as anna@contoso.com) | Must fix |
| Confidentiality | `Confidential.TenantHost` | Real SharePoint, Omnia or Azure host names (except contoso, tenant, ...) | Must fix |
| Confidentiality | `Confidential.InternalHost`, `Confidential.TestHost` | localhost, *.local, *.internal, dev/test/staging/demo hosts | Must fix |
| Confidentiality | `Confidential.InternalLink` | Links to private GitHub repositories, Azure DevOps, Trello, the Zendesk agent view | Must fix |
| Confidentiality | `Confidential.Guid`, `Confidential.IpAddress` | Tenant, app or object ids, IP addresses | Must fix |
| Confidentiality | `Reference.GitHubNumber`, `Reference.InternalTicket` | `(#4331)` with an internal GitHub card number, "PR #12", "AB#123" | Must fix |
| Confidentiality | `Reference.CustomerNumber` | `(#59036)`: listed so someone checks it is a Zendesk or OIM number | For information |
| Confidentiality | `Secrets.*` | Passwords, keys and tokens (gitleaks), in any file of the pull request | Must fix |
| Confidentiality | Images to look at | Every added or changed image, so a person checks screenshots for customer data | Listed in the comment |
| Structure | `Build.*` | New Sphinx build warnings: page not in any toctree, broken internal link or reference, missing image, broken heading markup | Must fix |
| Structure | `Links.Broken` | External links on changed lines that do not work (Sphinx linkcheck) | Please check |
| Structure | `Structure.ImageAlt` | `.. image::` or `.. figure::` without `:alt:` text | Please check |
| Structure | `Structure.UnusedImage` | Image file added but not used on any page | Please check |
| Structure | `Structure.HeadingLevel` | A heading that skips a level | Please check |

Confidentiality rules read the whole source, including rst comments and code samples: the repository is public,
so anyone can read them on GitHub. Tone rules read only the text that is shown on the site.

## Add or change a word or phrase

The phrase lists are plain files; no programming is needed.

| To change | Edit |
| --- | --- |
| Internal or sales language (blocks) | `vale/styles/Omnia/InternalLanguage.yml` |
| Unfinished text (blocks) | `vale/styles/Omnia/Leftovers.yml` |
| Marketing words (warning) | `vale/styles/Omnia/Superlatives.yml` |
| Future promises (warning) | `vale/styles/Omnia/FuturePromises.yml` |
| Email, host, GUID and ticket patterns and their allowed values | `confidentiality.yml` |
| Draft markers, files never checked, build warnings to ignore, link check | `settings.yml` |

Add one phrase per line under `tokens:`, for example `  - sales pitch`. Upper and lower case do not matter (except in
`Leftovers.yml`, where `TODO` must be upper case). `s?` at the end makes a word match with or without "s"; text in
`(?:...)` with `|` lists alternatives, for example `win (?:more )?deals?`. To move a phrase between "blocks" and
"warning", move it to the other file or change `level:` (`error` blocks, `warning` does not).

Open the change as a pull request: the workflow tests the lists against the examples in `tests/` before it uses them.
If a test fails after you added a phrase, a developer can update `tests/expected.yml`.

## When a finding is wrong (false positive)

Pick the smallest scope that works.

**A passage on one page.** Wrap it in rst comments; they are not shown on the site:

```rst
.. vale off

The phrase "key selling point" is quoted here on purpose.

.. vale on
```

**One rule for a passage.** Use the rule name from the review comment:

```rst
.. vale Confidential.Guid = NO

The app id of Omnia Feed 2 is ab4ee7fd-4aa2-494b-82a2-fe16b8f2c3ff.

.. vale Confidential.Guid = YES
```

**A value that is always fine** (a public app id, a placeholder tenant): add it under `allow:` of the pattern in
`confidentiality.yml`.

**A whole page or folder.** Add an entry under `suppress:` in `settings.yml`:

```yaml
suppress:
  - rule: Omnia.FuturePromises
    files: ['roadmap/**']
    reason: Roadmap pages describe future plans on purpose.
```

**A page that is intentionally not in any toctree:** add `:orphan:` as the first line of the page.

Secrets are never suppressed: if gitleaks finds a real secret, remove it and ask a developer to revoke it.

## Copilot review

`.github/instructions/docs-review.instructions.md` tells GitHub Copilot code review how to review `.rst` changes:
the reader of each section, internal-sounding text the phrase lists miss, promises, confidentiality and clear
wording, with suggested rewrites. Copilot reads the instructions from the pull request's branch, so changes to
that file apply to the pull request that makes them. Request a review with **Reviewers > Copilot** on the pull
request, or let a repository ruleset request it automatically.

## Run the checks on your computer

Needs Python 3.11 with `docs/requirements.txt` and `requirements.txt` from this folder installed,
[Vale](https://vale.sh/docs/install) 3.24 and [gitleaks](https://github.com/gitleaks/gitleaks/releases) 8.30, either on
`PATH` or set in `VALE_BIN` and `GITLEAKS_BIN`. Vale needs docutils' `rst2html.py`, which `docs/requirements.txt`
installs. From the repository root:

```bash
# test the rules against the examples in tests/
python .github/scripts/docs-review/test_docs_review.py

# review your branch (committed and uncommitted changes) like the pull request check
python .github/scripts/docs-review/docs_review.py --base origin/master

# review the files you name, completely
python .github/scripts/docs-review/docs_review.py --files pages/delete-page/index.rst --no-fail

# every page on the current checkout (slow; used for the baseline)
python .github/scripts/docs-review/docs_review.py --all --no-fail
```

The summary is written to `_build/docs-review/summary.md`.

## Limits

- Screenshots are not checked automatically; they are listed for a person to look at.
- Pull requests opened by the release-notes workflow with the default `GITHUB_TOKEN` do not start other workflows,
  so this check does not run on them by itself. Commits pushed straight to `master` (for example "Refresh documentation
  updates") are not reviewed at all.
- The test examples live in `tests/fixtures/` as `.rst.txt` files: Sphinx builds every `.rst` file in the repository,
  including under `.github/`, so real `.rst` files there would be published.
