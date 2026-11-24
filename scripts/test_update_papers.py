import unittest
from update_papers import merge, render, validate

PAPER = dict(id='arxiv:2611.12345', title='Loops <with> memory', authors=['A. Researcher'], year=2026,
             published='2026-11-24', url='https://arxiv.org/abs/2611.12345', family='Recurrent depth',
             curation='automatic', screen='keyword-screen')


class Updates(unittest.TestCase):
    def test_existing_manual_records_win_and_duplicates_do_not_grow(self):
        manual = dict(PAPER, title='Edited by an author', curation='human-reviewed')
        papers, candidates = merge([manual], [], [PAPER, PAPER], [])
        self.assertEqual(papers, [manual])
        self.assertEqual(candidates, [])

    def test_candidates_and_exclusions(self):
        pending = dict(PAPER, curation='needs-review', family=None)
        self.assertEqual(merge([], [], [pending], [], added_on='2026-11-24'), ([], [dict(pending, added_on='2026-11-24')]))
        self.assertEqual(merge([], [], [PAPER], [PAPER['id']]), ([], []))
        self.assertEqual(merge([], [dict(pending, added_on='2026-11-20')], [PAPER], [], added_on='2026-11-24'), ([dict(PAPER, added_on='2026-11-20')], []))

    def test_rejects_private_fields_or_unmatched_url(self):
        for invalid in [dict(PAPER, channel_id='private'), dict(PAPER, url='https://evil.invalid'), dict(PAPER, year='2026')]:
            with self.assertRaises(ValueError):
                validate(invalid)

    def test_output_escapes_metadata_and_has_no_empty_trailing_line(self):
        self.assertIn(r'Loops \<with\> memory', render([PAPER]))
        self.assertFalse(render([], True).endswith('\n\n'))


if __name__ == '__main__':
    unittest.main()
