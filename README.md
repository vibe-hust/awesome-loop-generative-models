# Awesome Loop Generative Models

An evolving paper list accompanying **Looping in Generative Models**. The list
covers recurrent depth, latent feedback, sample refinement, temporal memory,
and feedback between agent calls, together with relevant foundations and
comparisons. The initial bibliography contains 472 survey-selected works as of
24 November 2026; it is a narrative selection, not an exhaustive census.

- **[Paper list](PAPERS.md)** — survey selections and labeled automatic additions.
- **[Review queue](CANDIDATES.md)** — new papers whose relevance needs a person to check it.
- **[Machine-readable list](data/papers.json)** — stable IDs, titles, dates and primary links.

## Recent model reports

- [Inkling 2 Mini](https://thinkingmachines.ai/model-card/inkling-2-mini/)
- [GLM-5.4](https://z.ai/blog/glm-5.4)

## Updates and contributions

A worker in the existing Discord bot checks selected research channels every
30 minutes. It deduplicates arXiv links and verifies bibliographic identity
against the official abstract page. Explicit recurrent-depth matches and
high-confidence mechanism matches are marked **automatically screened**.
Other papers go into the review queue. Automatic screening can make mistakes;
inclusion is not verification of experimental results.

Only public paper metadata is copied here. Private messages, author discussions,
channel identifiers and credentials are not published. Non-arXiv reports can be
added manually. Old message edits and thread replies are not automatically rescanned.
The worker does not modify the survey manuscript.

To contribute, edit `data/papers.json` or `data/candidates.json`. Preserve stable
IDs (`arxiv:YYMM.NNNNN` without a version suffix, or a stable `source:` ID).
For approval, move a candidate to papers.json, assign a family, and set
`curation` to `human-reviewed`. To reject a paper permanently, put its ID in
`data/excluded.json` and remove its record from the lists. The bot regenerates
the Markdown indexes on its next update and preserves manually curated entries.
