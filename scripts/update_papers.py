"""Publish public metadata collected by the Railway Discord worker."""
import json
import os
from pathlib import Path
import re
import subprocess
import urllib.request
from datetime import datetime, timezone
from readme import update_readme

ROOT = Path(__file__).resolve().parents[1]
MANAGED = ['data/papers.json', 'data/candidates.json', 'PAPERS.md', 'CANDIDATES.md', 'README.md']
FAMILIES = ['Recurrent depth', 'Latent feedback', 'Sample refinement', 'Temporal memory', 'Agent feedback']


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def feed(payload):
    url = os.environ['LOOP_PAPERS_FEED_URL']
    if not url.startswith('https://'):
        raise ValueError('HTTPS feed required')
    request = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={
        'Authorization': 'Bearer ' + os.environ['LOOP_PAPERS_FEED_SECRET'],
        'Content-Type': 'application/json', 'User-Agent': 'LoopPapers-GitHubActions/1.0'})
    with urllib.request.build_opener(NoRedirect()).open(request, timeout=60) as response:
        raw = response.read(2_000_001)
    if len(raw) > 2_000_000:
        raise ValueError('Feed too large')
    return json.loads(raw)


def validate(paper):
    allowed = {'id', 'title', 'authors', 'year', 'published', 'url', 'family', 'curation', 'screen'}
    if not isinstance(paper, dict) or set(paper) - allowed:
        raise ValueError('Unexpected metadata fields')
    pid = paper.get('id', '')
    if not re.fullmatch(r'arxiv:(?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[a-z]{2})?/\d{7})', pid):
        raise ValueError('Invalid paper ID')
    if paper.get('url') != 'https://arxiv.org/abs/' + pid[6:]:
        raise ValueError('Paper URL does not match ID')
    if not isinstance(paper.get('title'), str) or not 1 <= len(paper['title']) <= 2000:
        raise ValueError('Invalid title')
    if type(paper.get('year')) is not int or not 1900 <= paper['year'] <= 2100:
        raise ValueError('Invalid year')
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', paper.get('published', '')):
        raise ValueError('Invalid publication date')
    if not isinstance(paper.get('authors'), list) or len(paper['authors']) > 5000 or any(not isinstance(a, str) or len(a) > 500 for a in paper['authors']):
        raise ValueError('Invalid authors')
    if paper.get('family') not in [None, *FAMILIES] or paper.get('curation') not in ['automatic', 'needs-review']:
        raise ValueError('Invalid curation')
    if paper.get('screen') not in ['keyword-screen', 'conservative-screen', 'metadata-model-screen']:
        raise ValueError('Invalid screen')
    return paper


def merge(papers, candidates, additions, excluded, added_on=None):
    accepted = {p['id']: p for p in papers}
    waiting = {p['id']: p for p in candidates}
    for raw in additions:
        p = validate(raw)
        if p['id'] in excluded or p['id'] in accepted:
            continue
        p = dict(p, added_on=added_on or datetime.now(timezone.utc).date().isoformat())
        if p['curation'] == 'automatic':
            accepted[p['id']] = dict(p, added_on=waiting.get(p['id'], {}).get('added_on', p['added_on']))
            waiting.pop(p['id'], None)
        else:
            waiting.setdefault(p['id'], p)
    return ordered(accepted.values()), ordered(waiting.values())


def ordered(papers):
    return sorted(papers, key=lambda p: (-p['year'], p['title'].casefold(), p['id']))


def markdown(value):
    return re.sub(r'([\\`*_\[\]<>|])', r'\\\1', re.sub(r'[\x00-\x1f\x7f]', ' ', value))


def render(papers, candidates=False):
    lines = ['# Papers awaiting relevance review' if candidates else '# Paper list', '',
             'Automatically collected public metadata. These papers are not yet part of the curated list.' if candidates else
             'Survey-selected papers and automatically screened additions. Inclusion does not imply that reported results have been reproduced.', '']
    year = None
    for p in ordered(papers):
        if p['year'] != year:
            year = p['year']
            lines.extend([f'## {year}', ''])
        if not re.match(r'https?://', p['url']) or re.search(r'[\s<>]', p['url']):
            raise ValueError('Invalid existing paper URL')
        suffix = ' — ' + markdown(p['family']) if p.get('family') else ''
        if p.get('curation') == 'automatic':
            suffix += ' · automatically screened'
        lines.append(f"- [{markdown(p['title'])}](<{p['url']}>){suffix}")
    return '\n'.join(lines).rstrip() + '\n'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, text=True).strip()


def main():
    read = lambda name: json.loads((ROOT / 'data' / (name + '.json')).read_text())
    papers, candidates, excluded = read('papers'), read('candidates'), read('excluded')
    response = feed({'action': 'sync', 'known': [p['id'] for p in papers + candidates], 'excluded': excluded})
    additions = response['papers']
    if not isinstance(additions, list) or len(additions) > 100:
        raise ValueError('Invalid batch')
    papers, candidates = merge(papers, candidates, additions, excluded)
    outputs = [json.dumps(papers, indent=2, ensure_ascii=False) + '\n',
               json.dumps(candidates, indent=2, ensure_ascii=False) + '\n', render(papers), render(candidates, True),
               update_readme((ROOT / 'README.md').read_text(), papers, candidates, read('reading_map'))]
    for path, text in zip(MANAGED, outputs):
        target = ROOT / path
        if target.is_symlink():
            raise ValueError('Managed files must not be symlinks')
        target.write_text(text)
    git('add', '--', *MANAGED)
    if git('diff', '--cached', '--name-only'):
        git('config', 'user.name', 'github-actions[bot]')
        git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
        git('commit', '-m', 'Update loop-model paper list from verified public metadata')
        # A concurrent human push fails here. Nothing is acknowledged; retry
        # merges the pending additions into a fresh checkout on the next run.
        git('push', 'origin', 'HEAD:main')
    sha = git('rev-parse', 'HEAD')
    if additions:
        feed({'action': 'ack', 'ids': [p['id'] for p in additions], 'sha': sha})
    print(json.dumps({'commit': sha, 'papers': len(papers), 'candidates': len(candidates), 'received': len(additions)}))


if __name__ == '__main__':
    main()
