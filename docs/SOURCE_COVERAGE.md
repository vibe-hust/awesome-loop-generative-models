# Source coverage audit

**Audited on 2026-11-24.** The collector and an independent history check covered
169 messages in the five configured research channels. Active and archived
thread discovery returned zero accessible threads, with no access or scan errors.
Thread collection is deployed for future posts and newly discoverable threads.

The messages contained **40 distinct arXiv papers** after removing version
suffixes and repeated links. After backfilling nine older omissions, all 40 are
accounted for:

| Status at audit time | Papers |
| :-- | --: |
| Already in the survey collection | 27 |
| In the separate relevance-review queue | 12 |
| Explicitly excluded by the curator | 1 |
| Unaccounted for | **0** |

The exclusion is [Code World Model 2.0](https://arxiv.org/abs/2611.22925).
It remains in `data/excluded.json` and does not appear in either reading list.

One additional OpenReview link was matched by its indexed title to
[Code World Models for General Game Playing](https://arxiv.org/abs/2510.04542),
which was already listed. It therefore does not add a distinct paper.
The [audit data](../data/source_audit.json) records the public identifiers and
the alias resolution. It contains no message text, author identities from
Discord, channel identifiers, or credentials.

## What the badges mean

- **Listed works:** all records in the main collection, initially 476 survey
  references. These include research papers, model reports, and background work.
- **Awaiting review:** additional records whose relevance has not yet been
  accepted. They appear separately in the README and are not in the main count.
- **Taxonomy families:** the five feedback mechanisms used by the survey.
  This is not a count of classified papers or collected channels.

The README groups the full collection by reading topic. Supporting references
have their own topics for foundations, training, and evaluation; a reading topic
does not by itself assert that every included method implements a loop.

## Limits

This is a dated audit of identifiable paper links in the configured channels,
including messages from all senders. It is not a census of the Discord server
or a claim that every listed work was posted in Discord. Image-only references,
deleted messages, inaccessible threads, and links without identifiable paper
metadata are outside this audit. The collector does not revisit edits to already
scanned messages; non-arXiv links require manual reconciliation.
