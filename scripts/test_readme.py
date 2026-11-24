import json
from pathlib import Path
import unittest
from readme import catalog_groups, link, render_sections, update_readme

ROOT = Path(__file__).resolve().parents[1]

class Readme(unittest.TestCase):
    def setUp(self):
        self.existing = (ROOT / 'README.md').read_text()
        self.papers = json.loads((ROOT / 'data/papers.json').read_text())
        self.groups = json.loads((ROOT / 'data/reading_map.json').read_text())

    def render(self, text, papers=None):
        return update_readme(text, self.papers if papers is None else papers, self.groups)

    def test_idempotence_and_preserving_curator_prose(self):
        text = 'An author note.\n\n' + self.existing + '\nKeep this afterword.\n'
        rendered = self.render(text)
        self.assertEqual(self.render(rendered), rendered)
        self.assertTrue(rendered.startswith('An author note.'))
        self.assertTrue(rendered.endswith('Keep this afterword.\n'))

    def test_unapproved_records_cannot_enter_public_readme(self):
        candidate = dict(id='arxiv:2611.99999', title='Private candidate', year=2026,
                         url='https://arxiv.org/abs/2611.99999', curation='needs-review', family='Temporal memory')
        with self.assertRaises(ValueError):
            self.render(self.existing, self.papers + [candidate])

    def test_missing_marker_or_reading_entry_fails(self):
        with self.assertRaises(ValueError):
            self.render(self.existing.replace('<!-- LOOP-BOT:RECENT:START -->', ''))
        missing = self.groups[0]['papers'][0]
        with self.assertRaises(ValueError):
            self.render(self.existing, papers=[p for p in self.papers if p['id'] != missing])

    def test_catalog_contains_every_published_work_once(self):
        catalog = render_sections(self.papers, self.groups)['CATALOG']
        grouped = [p['id'] for works in catalog_groups(self.papers).values() for p in works]
        self.assertCountEqual(grouped, [p['id'] for p in self.papers])
        for paper in self.papers:
            self.assertEqual(catalog.count(link(paper)), 1)
        excluded = json.loads((ROOT / 'data/excluded.json').read_text())
        self.assertFalse(set(excluded) & set(grouped))

    def test_public_copy_and_files_have_no_internal_queue_or_audit(self):
        rendered = self.render(self.existing)
        for term in ['awaiting review', 'needs review', 'review queue', 'CANDIDATES.md',
                     'source_audit', 'SOURCE_COVERAGE', 'docs/BOT.md', 'Discord', 'Railway']:
            self.assertNotIn(term.casefold(), rendered.casefold())
        for path in ['CANDIDATES.md', 'data/candidates.json', 'data/source_audit.json',
                     'docs/SOURCE_COVERAGE.md', 'docs/BOT.md']:
            self.assertFalse((ROOT / path).exists())

    def test_badges_count_only_published_references(self):
        stats = render_sections(self.papers, self.groups)['STATS']
        self.assertIn(f'listed works: {len(self.papers)}', stats)
        self.assertIn('feedback families: 5', stats)
        self.assertNotIn('review', stats.casefold())

    def test_family_or_curated_group_is_required_and_duplicates_are_rejected(self):
        paper = dict(id='arxiv:2611.99999', title='A <new> [paper]', year=2026,
                     url='https://arxiv.org/abs/2611.99999', family='Temporal memory', curation='automatic')
        self.assertEqual(catalog_groups([paper])['Temporal memory'], [paper])
        self.assertIn(r'A \<new\> \[paper\]', link(paper))
        for invalid in [[dict(paper, family=None)], [dict(paper, reading_group='Invented category')], [paper, paper]]:
            with self.assertRaises(ValueError):
                catalog_groups(invalid)

if __name__ == '__main__':
    unittest.main()
