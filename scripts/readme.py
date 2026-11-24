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
    'Related work to classify': 'Listed works whose reading topic has not yet been assigned.',
}


def slug(text):
    return re.sub(r'[^a-z0-9 -]', '', text.lower()).replace(' ', '-')


def catalog_groups(papers, candidates):
    ids = [p['id'] for p in papers + candidates]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate IDs across the collection and review queue')
    groups = {name: [] for name in GROUPS}
    for paper in papers:
        group = paper.get('reading_group') or paper.get('family') or 'Related work to classify'
        if group not in groups:
            raise ValueError(f'Unknown reading group: {group}')
        groups[group].append(paper)
    return {name: sorted(works, key=lambda p: (-p['year'], p['title'].casefold(), p['id']))
            for name, works in groups.items() if works}


def render_catalog(papers, candidates):
    groups = catalog_groups(papers, candidates)
    rows = ['| Reading topic | Listed works |', '| :-- | --: |']
    for name, works in groups.items():
        rows.append(f'| [{name}](#catalog-{slug(name)}) | {len(works)} |')
    rows.extend([f'| **Main collection** | **{len(papers)}** |',
                 f'| [Awaiting relevance review](#catalog-review) | {len(candidates)} |', ''])
    for name, works in groups.items():
        rows.extend([f'<a id="catalog-{slug(name)}"></a>',
                     f'<details><summary><strong>{name} · {len(works)} works</strong></summary>', '', GROUPS[name], ''])
        for paper in works:
            suffix = ' · Auto-screened' if paper.get('curation') == 'automatic' else ''
            rows.append(f"- **{paper['year']}** · {link(paper)}{suffix}")
        rows.extend(['', '</details>', ''])
    rows.extend(['<a id="catalog-review"></a>',
                 f'<details><summary><strong>Awaiting relevance review · {len(candidates)} works</strong></summary>', '',
                 'Metadata has been collected, but relevance and placement still need review. These works are excluded from the main collection count.', ''])
    for paper in sorted(candidates, key=lambda p: (-p['year'], p['title'].casefold(), p['id'])):
        rows.append(f"- **{paper['year']}** · {link(paper)} · Needs review")
    if not candidates:
        rows.append('No candidates are waiting for review.')
    rows.extend(['', '</details>'])
    return '\n'.join(rows)


def md(text):
    return re.sub(r'([\\`*_\[\]<>|])', r'\\\1', re.sub(r'[\x00-\x1f\x7f]', ' ', str(text)))


def link(paper):
    if not re.match(r'https?://', paper['url']) or re.search(r'[\s<>]', paper['url']):
        raise ValueError('Unsafe paper link')
    return f"[{md(paper['title'])}](<{paper['url']}>)"


def render_sections(papers, candidates, reading_map):
    index = {p['id']: p for p in papers}
    survey = sum(p.get('curation') == 'survey-selected' for p in papers)
    auto = sum(p.get('curation') == 'automatic' for p in papers)
    human = len(papers) - survey - auto
    def badge(label, value, color):
        url = f'https://img.shields.io/badge/{quote(label, safe="")}-{quote(str(value), safe="")}-{color}?style=flat-square'
        return f'  <img alt="{label}: {value}" src="{url}">'
    stats = '\n'.join(['<p align="center">', badge('listed works', len(papers), '157f79'),
                        badge('awaiting review', len(candidates), 'ba7a29'), badge('taxonomy families', len(reading_map), '6557a8'),
                        '</p>', '', f'**{len(papers)} listed works** in the main collection · **{len(candidates)} awaiting review** (counted separately).', '',
                        f'The main collection contains {survey} survey references, {human} human-reviewed additions, and {auto} automatically screened additions. '
                        'It includes papers, model reports, and background references; this is not a count of papers collected from Discord. '
                        'The five families describe the taxonomy, with additional reading topics for foundations, training, and evaluation.'])
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
            'RECENT': '\n'.join(rows), 'OVERSIGHT': '\n'.join(oversight), 'CATALOG': render_catalog(papers, candidates)}


def update_readme(existing, papers, candidates, reading_map):
    for section, content in render_sections(papers, candidates, reading_map).items():
        start, end = f'<!-- LOOP-BOT:{section}:START -->', f'<!-- LOOP-BOT:{section}:END -->'
        if existing.count(start) != 1 or existing.count(end) != 1 or existing.index(start) > existing.index(end):
            raise ValueError(f'Missing or duplicated README markers: {section}')
        before, rest = existing.split(start, 1)
        _, after = rest.split(end, 1)
        existing = before + start + '\n' + content + '\n' + end + after
    return existing
