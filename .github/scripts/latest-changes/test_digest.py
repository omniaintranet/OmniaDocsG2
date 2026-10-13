"""Behavioral tests for reader output, retries, grouping, and API boundaries."""

from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('digest', Path(__file__).with_name('update.py'))
digest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(digest)


class DigestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write('guide/index.rst', 'Example guide\n=============\n\n.. image:: shot.png\n')
        self.write(digest.DIGEST, 'Initial page\n')
        self.state = self.root / 'state.json'
        self.state.write_text(json.dumps({'version': 1, 'processed': {}, 'entries': []}))
        self.now = datetime(2026, 10, 13, 10, tzinfo=timezone.utc)
        self.pr = {'number': 4, 'merged_at': '2026-10-13T06:00:00Z'}

    def write(self, name, text):
        file = self.root / name
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text, encoding='utf-8')

    def update(self, prs, files, classifier):
        with patch.object(digest, 'ROOT', self.root), patch.object(digest, 'STATE', self.state), \
             patch.dict(digest.os.environ, GITHUB_REPOSITORY='owner/docs', DOCS_BRANCH='master'), \
             patch.object(digest, 'merged_prs', return_value=prs), \
             patch.object(digest, 'pr_files', side_effect=lambda repo, pr: files[pr['number']]), \
             patch.object(digest, 'classify', side_effect=classifier):
            digest.update(self.now)

    def test_local_calendar_window(self):
        now = datetime(2026, 10, 12, 23, 30, tzinfo=timezone.utc)
        self.assertEqual(digest.cutoff_for(now).isoformat(), '2026-09-14')

    def test_image_and_nested_include_dependencies(self):
        self.write('guide/index.rst', 'Example guide\n=============\n\n.. include:: snippets/extra.txt\n')
        self.write('guide/snippets/extra.txt', '.. include:: detail.txt\n')
        self.write('guide/snippets/detail.txt', '.. |image| image:: ../shot.png\n')
        pages = digest.pages_in(self.root)
        dependencies = digest.dependency_map(self.root, pages)
        self.assertEqual(dependencies['guide/shot.png'], {'guide/index.rst'})
        groups = digest.collect_groups(self.pr, [{'filename': 'guide/shot.png', 'status': 'modified'}],
                                       pages, dependencies, lambda f: {'path': f['filename'], 'status': 'modified'})
        self.assertEqual(len(groups), 1)
        group = next(iter(groups.values()))
        self.assertEqual(digest.classify(group, pages['guide/index.rst'])['classification'], 'Updated screenshots')

    def test_reader_output_has_titles_classifications_descriptions_only(self):
        pages = digest.pages_in(self.root)
        entries = [{'date': '2026-10-13', 'path': 'guide/index.rst',
                    'classification': 'Added information', 'description': 'Added an example.', 'pr': 123}]
        text = digest.render(entries, pages)
        self.assertIn('Example guide <https://omnia-docs-g2.readthedocs.io/en/latest/guide/index.html>', text)
        self.assertIn('**Added information**', text)
        self.assertIn('Added an example.', text)
        self.assertNotIn('123', text)
        self.assertNotIn('github', text.lower())
        self.assertNotIn('pull request', text.lower())

    def test_release_history_uses_a_stable_reader_title(self):
        self.write('release-notes/7.0/versions.rst', '7.11.32\n=======\n\nRelease notes.\n')
        pages = digest.pages_in(self.root)
        self.assertEqual(pages['release-notes/7.0/versions.rst']['title'], 'Omnia 7 release notes')

    def test_same_page_day_combined_and_repeat_run_does_not_reclassify(self):
        other = {**self.pr, 'number': 5}
        files = {number: [{'filename': 'guide/index.rst', 'status': 'modified', 'patch': '@@\n-old\n+new'}]
                 for number in (4, 5)}
        calls = []

        def classifier(group, page, previous):
            calls.append(group)
            return {'classification': 'Added information', 'description': 'Added an example.'}

        self.update([self.pr, other], files, classifier)
        self.assertEqual(len(calls), 1)
        self.assertEqual(len(calls[0]['changes']), 2)
        initial = self.state.read_text()
        self.update([self.pr, other], files, lambda *args: self.fail('Repeated classification'))
        self.assertEqual(self.state.read_text(), initial)
        self.assertEqual(len(json.loads(initial)['entries']), 1)

    def test_later_same_day_change_receives_previous_entry(self):
        files = {4: [{'filename': 'guide/index.rst', 'status': 'modified', 'patch': '+example'}],
                 5: [{'filename': 'guide/shot.png', 'status': 'modified'}]}
        result = {'classification': 'Added information', 'description': 'Added an example.'}
        self.update([self.pr], files, lambda *args: result)
        previous = []
        self.update([self.pr, {**self.pr, 'number': 5}], files,
                    lambda group, page, old: previous.append(old) or result)
        self.assertEqual(previous, [{'date': '2026-10-13', 'path': 'guide/index.rst', **result}])

    def test_failure_leaves_both_files_unchanged(self):
        state_before = self.state.read_text()
        page_before = (self.root / digest.DIGEST).read_text()
        files = {4: [{'filename': 'guide/index.rst', 'status': 'modified', 'patch': '+example'}]}

        def failure(*args):
            raise ValueError('Invalid classification')

        with self.assertRaises(ValueError):
            self.update([self.pr], files, failure)
        self.assertEqual(self.state.read_text(), state_before)
        self.assertEqual((self.root / digest.DIGEST).read_text(), page_before)
        self.update([self.pr], files, lambda *args: {'classification': 'Correction', 'description': 'Corrected a setting.'})
        self.assertIn('4', json.loads(self.state.read_text())['processed'])

    def test_expired_and_deleted_pages_are_removed(self):
        state = {'version': 1, 'processed': {'1': '2026-09-13'}, 'entries': [
            {'date': '2026-09-13', 'path': 'guide/index.rst'},
            {'date': '2026-10-12', 'path': 'deleted/index.rst'}]}
        self.state.write_text(json.dumps(state))
        self.update([], {}, lambda *args: self.fail('No changes'))
        self.assertEqual(json.loads(self.state.read_text())['entries'], [])
        self.assertEqual(json.loads(self.state.read_text())['processed'], {})

    def test_digest_and_automation_do_not_report_themselves(self):
        pages = digest.pages_in(self.root)
        files = [{'filename': path, 'status': 'modified'} for path in
                 (digest.DIGEST, 'index.rst', '.github/scripts/latest-changes/state.json')]
        groups = digest.collect_groups(self.pr, files, pages, {}, lambda f: self.fail('Excluded change'))
        self.assertEqual(groups, {})

    def test_new_page_classification_cannot_be_downgraded(self):
        group = {'new': True, 'changes': [{'diff': '+New guidance'}]}
        response = json.dumps({'classification': 'Spelling / grammar', 'description': 'Added guidance for configuration.'})
        with patch.object(digest, 'command', return_value=response):
            result = digest.classify(group, {'title': 'Guide', 'text': 'Guide\n=====\n'})
        self.assertEqual(result['classification'], 'New page')

    def test_classifier_rejects_links_and_git_provenance(self):
        for description in ['See https://example.com', 'Merged PR #42.', 'Changed the GitHub repository.', 'First\nSecond']:
            with self.subTest(description=description), self.assertRaises(ValueError):
                digest.plain_text(description, 180)

    def test_long_page_context_does_not_discard_the_actual_diff(self):
        group = {'new': False, 'changes': [{'diff': '+Added an example.'}]}
        response = json.dumps({'classification': 'Added information', 'description': 'Added an example.'})
        with patch.object(digest, 'command', return_value=response) as command:
            digest.classify(group, {'title': 'Long history', 'text': 'Existing text.\n' * 20000})
        prompt = command.call_args.kwargs['input']
        self.assertIn('+Added an example.', prompt)
        self.assertLess(len(prompt), 40000)

    def test_overlong_model_description_is_corrected_before_publication(self):
        group = {'new': False, 'changes': [{'diff': '+Added an example.'}]}
        invalid = json.dumps({'classification': 'Added information', 'description': 'Long description. ' * 20})
        valid = json.dumps({'classification': 'Added information', 'description': 'Added an example.'})
        with patch.object(digest, 'command', side_effect=[invalid, valid]) as command:
            result = digest.classify(group, {'title': 'Guide', 'text': 'Guide\n=====\n'})
        self.assertEqual(command.call_count, 2)
        self.assertEqual(result['description'], 'Added an example.')

    def test_rename_updates_previous_links(self):
        entry = {'date': '2026-10-12', 'path': 'old/index.rst',
                 'classification': 'Added information', 'description': 'Added an example.'}
        self.state.write_text(json.dumps({'version': 1, 'processed': {}, 'entries': [entry]}))
        files = {4: [{'status': 'renamed', 'previous_filename': 'old/index.rst',
                      'filename': 'guide/index.rst', 'patch': '+New location'}]}
        self.update([self.pr], files, lambda *args: {'classification': 'Navigation update', 'description': 'Moved this guide.'})
        self.assertEqual({e['path'] for e in json.loads(self.state.read_text())['entries']}, {'guide/index.rst'})
        self.assertNotIn('old/index.html', (self.root / digest.DIGEST).read_text())

    def test_backfill_before_rename_keeps_the_new_page_and_current_link(self):
        files = {4: [{'filename': 'old/index.rst', 'status': 'added', 'patch': '+Guide'}],
                 5: [{'filename': 'guide/index.rst', 'status': 'renamed', 'previous_filename': 'old/index.rst', 'patch': '+Example'}]}
        calls = []

        def classify(group, page, previous):
            calls.append(group)
            return {'classification': 'New page', 'description': 'Added a guide.'}

        self.update([self.pr, {**self.pr, 'number': 5}], files, classify)
        self.assertEqual(len(calls), 1)
        self.assertTrue(calls[0]['new'])
        self.assertEqual(len(calls[0]['changes']), 2)
        self.assertEqual(calls[0]['path'], 'guide/index.rst')

    def test_missing_text_patch_retrieves_both_sides(self):
        pr = {**self.pr, 'base': {'sha': 'before'}, 'head': {'sha': 'after'}}
        with patch.object(digest, 'command', side_effect=['Old text\n', 'New text\n']) as command:
            evidence = digest.change_evidence('owner/docs', pr, {'filename': 'guide/index.rst', 'status': 'modified'})
        self.assertEqual(command.call_count, 2)
        self.assertIn('-Old text', evidence['diff'])
        self.assertIn('+New text', evidence['diff'])

    def test_generated_rst_parses_and_has_one_published_link(self):
        from docutils.core import publish_doctree
        from docutils import nodes
        pages = digest.pages_in(self.root)
        entries = [{'date': '2026-10-13', 'path': 'guide/index.rst',
                    'classification': 'Updated guidance', 'description': 'Changed *configuration* guidance.'}]
        tree = publish_doctree(digest.render(entries, pages))
        self.assertEqual(len(list(tree.findall(nodes.system_message))), 0)
        links = list(tree.findall(nodes.reference))
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]['refuri'], 'https://omnia-docs-g2.readthedocs.io/en/latest/guide/index.html')

    def test_merge_filter_handles_recent_updates_to_old_prs(self):
        def pr(number, merged, updated, branch='master'):
            return {'number': number, 'merged_at': merged, 'updated_at': updated,
                    'base': {'ref': branch}, 'merge_commit_sha': str(number)}
        batch = [pr(1, None, '2026-10-13T09:00:00Z'),
                 pr(2, '2026-09-01T09:00:00Z', '2026-10-13T09:00:00Z'),
                 pr(3, '2026-10-12T09:00:00Z', '2026-10-12T09:00:00Z', 'other'),
                 pr(4, '2026-10-12T09:00:00Z', '2026-10-12T09:00:00Z')]
        with patch.object(digest, 'api', side_effect=[batch, []]), \
             patch.object(digest.subprocess, 'run') as run:
            run.return_value.returncode = 0
            found = digest.merged_prs('owner/docs', 'master', digest.cutoff_for(self.now), self.now)
        self.assertEqual([p['number'] for p in found], [4])

    def test_large_pr_fails_instead_of_silently_truncating(self):
        with patch.object(digest, 'api', return_value=[{'filename': 'file'}] * 100), self.assertRaises(ValueError):
            digest.pr_files('owner/docs', self.pr)


if __name__ == '__main__':
    unittest.main()
