import json
from pathlib import Path
import unittest
from readme import catalog_groups, link, render_sections, update_readme

ROOT = Path(__file__).resolve().parents[1]


class Readme(unittest.TestCase):
    def setUp(self):
        self.existing = (ROOT / 'README.md').read_text()
        self.papers = json.loads((ROOT / 'data/papers.json').read_text())
        self.candidates = json.loads((ROOT / 'data/candidates.json').read_text())
        self.groups = json.loads((ROOT / 'data/reading_map.json').read_text())

    def render(self, text, papers=None, candidates=None):
        return update_readme(text, self.papers if papers is None else papers,
                             self.candidates if candidates is None else candidates, self.groups)

    def test_idempotence_and_preserving_curator_prose(self):
        text = 'An author note.\n\n' + self.existing + '\nKeep this afterword.\n'
        rendered = self.render(text)
        self.assertEqual(self.render(rendered), rendered)
        self.assertTrue(rendered.startswith('An author note.'))
        self.assertTrue(rendered.endswith('Keep this afterword.\n'))

    def test_new_candidate_updates_counts_and_recent_without_claiming_acceptance(self):
        candidate = dict(id='arxiv:2611.99999', title='A <new> [candidate]', year=2026,
                         url='https://arxiv.org/abs/2611.99999', curation='needs-review', added_on='2099-01-01')
        rendered = self.render(self.existing, candidates=self.candidates + [candidate])
        self.assertIn(f'**{len(self.candidates)+1} awaiting review**', rendered)
        self.assertIn(r'A \<new\> \[candidate\]', rendered)
        self.assertIn('| Needs review |', rendered)

    def test_missing_marker_or_missing_reading_entry_fails_without_rewriting(self):
        with self.assertRaises(ValueError):
            self.render(self.existing.replace('<!-- LOOP-BOT:RECENT:START -->', ''))
        missing = self.groups[0]['papers'][0]
        with self.assertRaises(ValueError):
            self.render(self.existing, papers=[p for p in self.papers if p['id'] != missing])

    def test_full_catalog_contains_every_work_once_and_separates_review(self):
        catalog = render_sections(self.papers, self.candidates, self.groups)['CATALOG']
        accepted, waiting = catalog.split('<a id="catalog-review"></a>')
        grouped = [p['id'] for works in catalog_groups(self.papers, self.candidates).values() for p in works]
        self.assertCountEqual(grouped, [p['id'] for p in self.papers])
        for paper in self.papers:
            self.assertEqual(accepted.count(link(paper)), 1)
            self.assertNotIn(link(paper), waiting)
        for paper in self.candidates:
            self.assertNotIn(link(paper), accepted)
            self.assertEqual(waiting.count(link(paper)), 1)
        excluded = json.loads((ROOT / 'data/excluded.json').read_text())
        self.assertFalse(set(excluded) & {p['id'] for p in self.papers + self.candidates})

    def test_counts_describe_collection_and_taxonomy_without_claiming_channel_coverage(self):
        stats = render_sections(self.papers, self.candidates, self.groups)['STATS']
        self.assertIn(f'listed works: {len(self.papers)}', stats)
        self.assertIn('taxonomy families: 5', stats)
        self.assertIn('not a count of papers collected from Discord', stats)

    def test_new_screened_family_and_unknown_topic_are_handled_explicitly(self):
        paper = dict(id='arxiv:2611.99999', title='New paper', year=2026,
                     url='https://arxiv.org/abs/2611.99999', family='Temporal memory', curation='automatic')
        self.assertEqual(catalog_groups([paper], [])['Temporal memory'], [paper])
        unclassified = dict(paper, family=None)
        self.assertEqual(catalog_groups([unclassified], [])['Related work to classify'], [unclassified])
        with self.assertRaises(ValueError):
            catalog_groups([dict(paper, reading_group='Invented category')], [])
        with self.assertRaises(ValueError):
            catalog_groups([paper], [paper])

    def test_source_audit_has_no_unaccounted_identifiers(self):
        audit = json.loads((ROOT / 'data/source_audit.json').read_text())
        known = {p['id'] for p in self.papers + self.candidates}
        excluded = set(json.loads((ROOT / 'data/excluded.json').read_text()))
        shared = set(audit['paper_ids'])
        self.assertEqual(len(shared), audit['unique_papers'])
        self.assertFalse(shared - known - excluded)
        for alias in audit['other_primary_links']:
            self.assertIn(alias['paper_id'], known | excluded)


if __name__ == '__main__':
    unittest.main()
