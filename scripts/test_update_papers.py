import contextlib
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import update_papers
from update_papers import merge, publishable, render, validate

PAPER = dict(id='arxiv:2611.12345', title='Loops <with> memory', authors=['A. Researcher'], year=2026,
             published='2026-11-24', url='https://arxiv.org/abs/2611.12345', family='Recurrent depth',
             curation='automatic', screen='keyword-screen')

class Updates(unittest.TestCase):
    def test_existing_editorial_records_win_and_duplicates_do_not_grow(self):
        manual = dict(PAPER, title='Edited by a curator', curation='reviewed', summary='Curated description')
        self.assertEqual(merge([manual], [PAPER, PAPER], []), [manual])

    def test_uncertain_and_excluded_records_do_not_publish(self):
        pending = dict(PAPER, curation='needs-review', family=None)
        self.assertEqual(publishable([pending]), [])
        self.assertEqual(merge([], [pending], []), [])
        self.assertEqual(merge([], [PAPER], [PAPER['id']]), [])
        self.assertEqual(merge([], [PAPER], [], added_on='2026-11-24'), [dict(PAPER, added_on='2026-11-24')])
        with self.assertRaises(ValueError):
            render([pending])

    def test_rejects_private_fields_or_unmatched_url(self):
        for invalid in [dict(PAPER, channel_id='private'), dict(PAPER, url='https://evil.invalid'), dict(PAPER, year='2026')]:
            with self.assertRaises(ValueError):
                validate(invalid)

    def test_output_escapes_metadata(self):
        self.assertIn(r'Loops \<with\> memory', render([PAPER]))
        self.assertFalse(render([]).endswith('\n\n'))

    def test_older_mixed_feed_cannot_publish_or_ack_private_candidates(self):
        original = update_papers.ROOT
        pending = dict(PAPER, id='arxiv:2611.99999', url='https://arxiv.org/abs/2611.99999',
                       title='PRIVATE REVIEW TITLE', curation='needs-review', family=None)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'data').mkdir()
            for relative in ['README.md', 'data/papers.json', 'data/excluded.json', 'data/reading_map.json']:
                shutil.copy2(original / relative, root / relative)
            with patch.object(update_papers, 'ROOT', root), patch.object(update_papers, 'feed') as feed, patch.object(update_papers, 'git', side_effect=lambda *args: 'a' * 40 if args[0]=='rev-parse' else ''), contextlib.redirect_stdout(io.StringIO()):
                feed.side_effect = [{'papers':[pending,PAPER]}, {'acknowledged':True}]
                update_papers.main()
            self.assertEqual(feed.call_args_list[-1].args[0]['ids'], [PAPER['id']])
            for relative in update_papers.MANAGED:
                self.assertNotIn('PRIVATE REVIEW TITLE', (root / relative).read_text())
            self.assertFalse((root / 'data/candidates.json').exists())
            self.assertFalse((root / 'CANDIDATES.md').exists())
            public = json.loads((root / 'data/papers.json').read_text())
            self.assertIn(PAPER['id'], {p['id'] for p in public})
            self.assertNotIn(pending['id'], {p['id'] for p in public})

if __name__ == '__main__':
    unittest.main()
