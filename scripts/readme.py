"""Refresh bounded README sections while preserving the curator's prose."""
import re
from urllib.parse import quote

OVERSIGHT = ['arxiv:2507.11473', 'arxiv:2503.11926', 'arxiv:2505.05410', 'arxiv:2512.18311']


def md(text):
    return re.sub(r'([\\`*_\[\]<>|])', r'\\\1', re.sub(r'[\x00-\x1f\x7f]', ' ', str(text)))


def link(paper):
    if not re.match(r'https?://', paper['url']) or re.search(r'[\s<>]', paper['url']):
        raise ValueError('Unsafe paper link')
    return f"[{md(paper['title'])}](<{paper['url']}>)"


def render_sections(papers, candidates, reading_map):
    index = {p['id']: p for p in papers}
    human = sum(p.get('curation') != 'automatic' for p in papers)
    auto = len(papers) - human
    def badge(label, value, color):
        url = f'https://img.shields.io/badge/{quote(label, safe="")}-{quote(str(value), safe="")}-{color}?style=flat-square'
        return f'  <img alt="{label}: {value}" src="{url}">'
    stats = '\n'.join(['<p align="center">', badge('papers', len(papers), '157f79'),
                        badge('awaiting review', len(candidates), 'ba7a29'), badge('feedback families', 5, '6557a8'),
                        '</p>', '', f'**{len(papers)} papers** · {human} survey-selected or human-reviewed · {auto} automatically screened · **{len(candidates)} awaiting review**'])
    taxonomy = ['| Family | What returns to computation? | Question to ask |', '| :-- | :-- | :-- |']
    reading = []
    if len(reading_map) != 5:
        raise ValueError('The curated reading map must contain five families')
    for number, group in enumerate(reading_map, 1):
        slug = re.sub(r'[^a-z0-9 -]', '', group['family'].lower()).replace(' ', '-')
        taxonomy.append(f"| **[{md(group['family'])}](#{number}-{slug})** | {md(group['state'])} | {md(group['question'])} |")
        reading.extend([f"### {number}. {group['family']}", '', group['question'], ''])
        for pid in group['papers']:
            if pid not in index:
                raise ValueError(f'Reading-map paper is missing: {pid}')
            paper = index[pid]
            reading.append(f"- **{paper['year']}** · {link(paper)}")
        reading.append('')
    recent = sorted([p for p in papers + candidates if p.get('added_on')],
                    key=lambda p: (p['added_on'], p.get('published', str(p['year'])), p['id']), reverse=True)[:10]
    rows = ['| Added | Paper | Status |', '| :-- | :-- | :-- |']
    for paper in recent:
        state = {'automatic': 'Auto-screened', 'needs-review': 'Needs review'}.get(paper.get('curation'), 'Curated')
        rows.append(f"| {md(paper['added_on'])} | {link(paper)} | {state} |")
    if not recent:
        rows = ['The initial collection is ready. New additions will appear here after the next update.']
    rows.extend(['', '[Browse all papers →](PAPERS.md) · [Help review candidates →](CANDIDATES.md)'])
    oversight = [f"- **{index[pid]['year']}** · {link(index[pid])}" for pid in OVERSIGHT if pid in index]
    return {'STATS': stats, 'TAXONOMY': '\n'.join(taxonomy), 'READING': '\n'.join(reading).rstrip(),
            'RECENT': '\n'.join(rows), 'OVERSIGHT': '\n'.join(oversight)}


def update_readme(existing, papers, candidates, reading_map):
    for section, content in render_sections(papers, candidates, reading_map).items():
        start, end = f'<!-- LOOP-BOT:{section}:START -->', f'<!-- LOOP-BOT:{section}:END -->'
        if existing.count(start) != 1 or existing.count(end) != 1 or existing.index(start) > existing.index(end):
            raise ValueError(f'Missing or duplicated README markers: {section}')
        before, rest = existing.split(start, 1)
        _, after = rest.split(end, 1)
        existing = before + start + '\n' + content + '\n' + end + after
    return existing
