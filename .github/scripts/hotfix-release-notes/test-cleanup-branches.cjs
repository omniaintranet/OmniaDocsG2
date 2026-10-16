// Offline checks for the cleanup workflow. Run with node --test on this file.
const { readFileSync } = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { test } = require('node:test');
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
const workflow = readFileSync(path.resolve(__dirname, '../../workflows/cleanup-hotfix-release-note-branches.yml'), 'utf8');
const source = workflow.split('          script: |\n')[1].split('\n').map(line => line.slice(12)).join('\n');
const execute = new AsyncFunction('context', 'github', 'core', source);

async function run({ merged = true, base = 'master', branch = 'hotfix-release-notes-7.11.33',
    repo = 'omniaintranet/OmniaDocsG2', currentSha = 'merged-head', error } = {}) {
  const calls = [];
  const context = {
    repo: { owner: 'omniaintranet', repo: 'OmniaDocsG2' },
    payload: { pull_request: {
      merged, base: { ref: base },
      head: { ref: branch, sha: 'merged-head', repo: repo ? { full_name: repo } : null }
    } }
  };
  const github = { rest: { git: {
    getRef: async params => {
      calls.push(['get', params]);
      if (error) throw error;
      return { data: { object: { sha: currentSha } } };
    },
    deleteRef: async params => { calls.push(['delete', params]); }
  } } };
  await execute(context, github, { info() {}, warning() {} });
  return calls;
}

test('deletes only the matching merged branch in the documentation repo', async () => {
  assert.deepEqual(await run(), [
    ['get', { owner: 'omniaintranet', repo: 'OmniaDocsG2', ref: 'heads/hotfix-release-notes-7.11.33' }],
    ['delete', { owner: 'omniaintranet', repo: 'OmniaDocsG2', ref: 'heads/hotfix-release-notes-7.11.33' }]
  ]);
});

for (const [name, options] of [
  ['unmerged PR', { merged: false }],
  ['unrelated branch', { branch: 'codex/other-change' }],
  ['invalid version', { branch: 'hotfix-release-notes-7.11.33/other' }],
  ['other base branch', { base: 'other' }],
  ['fork branch', { repo: 'someone/OmniaDocsG2' }],
  ['deleted fork', { repo: null }]
]) {
  test(`ignores ${name} without API mutations`, async () => assert.deepEqual(await run(options), []));
}

test('keeps a branch that has changed since the merged PR', async () => {
  const calls = await run({ currentSha: 'new-work' });
  assert.equal(calls.length, 1);
  assert.equal(calls[0][0], 'get');
});

test('already deleted branches are harmless', async () => {
  const calls = await run({ error: { status: 404 } });
  assert.equal(calls.length, 1);
});

test('reports other GitHub API failures', async () => {
  await assert.rejects(run({ error: new Error('API unavailable') }), /API unavailable/);
});
