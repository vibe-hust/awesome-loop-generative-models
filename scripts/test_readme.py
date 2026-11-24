import json
from pathlib import Path
import unittest
from readme import update_readme

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


if __name__ == '__main__':
    unittest.main()
