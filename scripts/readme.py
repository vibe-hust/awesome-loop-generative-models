"""Refresh bounded README sections while preserving the curator's prose."""
import re
from urllib.parse import quote

OVERSIGHT = ['arxiv:2507.11473', 'arxiv:2503.11926', 'arxiv:2505.05410', 'arxiv:2512.18311']
GROUPS = {
    'Recurrent depth': 'Shared blocks, adaptive depth, fixed points, and recurrent reasoning.',
    'Latent feedback': 'Hidden-state reasoning and feedback across token positions.',
    'Sample refinement': 'Iterative generation, self-conditioning, and related sampling methods.',
    'Temporal memory': 'Persistent state, sequence models, and memory in video world models.',
    'Agent feedback': 'Critique, search, tool use, and feedback between model calls.',
    'Foundations and related models': 'Theory, surveys, parameter sharing, and comparison architectures.',
    'Training and execution': 'Learning objectives, distillation, caching, and efficient inference.',
    'Evaluation and interpretability': 'Benchmarks, controlled comparisons, mechanisms, and oversight.',
}


def slug(text):
    return re.sub(r'[^a-z0-9 -]', '', text.lower()).replace(' ', '-')


def catalog_groups(papers):
    ids = [p['id'] for p in papers]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate IDs in the collection')
    groups = {name: [] for name in GROUPS}
    for paper in papers:
        if paper.get('curation') == 'needs-review':
            raise ValueError('Unapproved metadata cannot enter public output')
        group = paper.get('reading_group') or paper.get('family')
        if group not in groups:
            raise ValueError(f'Unknown reading group: {group}')
        groups[group].append(paper)
    return {name: sorted(works, key=lambda p: (-p['year'], p['title'].casefold(), p['id']))
            for name, works in groups.items() if works}


def render_catalog(papers):
    groups = catalog_groups(papers)
    rows = ['| Reading topic | Listed works |', '| :-- | --: |']
    for name, works in groups.items():
        rows.append(f'| [{name}](#catalog-{slug(name)}) | {len(works)} |')
    rows.extend([f'| **Total** | **{len(papers)}** |', ''])
    for name, works in groups.items():
        rows.extend([f'<a id="catalog-{slug(name)}"></a>',
                     f'### {name} · {len(works)} works', '', GROUPS[name], ''])
        for paper in works:
            suffix = ' — ' + md(paper['summary']) if paper.get('summary') else ''
            rows.append(f"- **{paper['year']}** · {link(paper)}{suffix}")
        rows.append('')
    return '\n'.join(rows).rstrip()


def md(text):
    return re.sub(r'([\\`*_\[\]<>|])', r'\\\1', re.sub(r'[\x00-\x1f\x7f]', ' ', str(text)))


def link(paper):
    if not re.match(r'https?://', paper['url']) or re.search(r'[\s<>]', paper['url']):
        raise ValueError('Unsafe paper link')
    return f"[{md(paper['title'])}](<{paper['url']}>)"


def render_sections(papers, reading_map):
    index = {p['id']: p for p in papers}
    def badge(label, value, color):
        url = f'https://img.shields.io/badge/{quote(label, safe="")}-{quote(str(value), safe="")}-{color}?style=flat-square'
        return f'  <img alt="{label}: {value}" src="{url}">'
    stats = '\n'.join(['<p align="center">', badge('listed works', len(papers), '157f79'),
                        badge('feedback families', len(reading_map), '6557a8'),
                        '</p>', '', f'**{len(papers)} research papers, model reports, and supporting references**, '
                        'organized around five feedback families and related topics.'])
    taxonomy = ['| Family | What returns to computation? | Question to ask |', '| :-- | :-- | :-- |']
    reading = []
    if len(reading_map) != 5:
        raise ValueError('The curated reading map must contain five families')
    for number, group in enumerate(reading_map, 1):
        family_slug = slug(group['family'])
        taxonomy.append(f"| **[{md(group['family'])}](#{number}-{family_slug})** | {md(group['state'])} | {md(group['question'])} |")
        reading.extend([f"### {number}. {group['family']}", '', group['question'], ''])
        for pid in group['papers']:
            if pid not in index:
                raise ValueError(f'Reading-map paper is missing: {pid}')
            paper = index[pid]
            reading.append(f"- **{paper['year']}** · {link(paper)}")
        reading.append('')
    recent = sorted([p for p in papers if p.get('added_on')],
                    key=lambda p: (p['added_on'], p.get('published', str(p['year'])), p['id']), reverse=True)[:10]
    rows = ['| Added | Paper | Reading topic |', '| :-- | :-- | :-- |']
    for paper in recent:
        topic = paper.get('reading_group') or paper.get('family')
        rows.append(f"| {md(paper['added_on'])} | {link(paper)} | {md(topic)} |")
    if not recent:
        rows = ['The initial collection is ready. New additions will appear here after the next update.']
    rows.extend(['', '[Browse the complete bibliography →](PAPERS.md)'])
    oversight = [f"- **{index[pid]['year']}** · {link(index[pid])}" for pid in OVERSIGHT if pid in index]
    return {'STATS': stats, 'TAXONOMY': '\n'.join(taxonomy), 'READING': '\n'.join(reading).rstrip(),
            'RECENT': '\n'.join(rows), 'OVERSIGHT': '\n'.join(oversight), 'CATALOG': render_catalog(papers)}


def update_readme(existing, papers, reading_map):
    for section, content in render_sections(papers, reading_map).items():
        start, end = f'<!-- LOOP-BOT:{section}:START -->', f'<!-- LOOP-BOT:{section}:END -->'
        if existing.count(start) != 1 or existing.count(end) != 1 or existing.index(start) > existing.index(end):
            raise ValueError(f'Missing or duplicated README markers: {section}')
        before, rest = existing.split(start, 1)
        _, after = rest.split(end, 1)
        existing = before + start + '\n' + content + '\n' + end + after
    return existing
