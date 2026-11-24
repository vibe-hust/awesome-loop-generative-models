# Bot mission and maintenance

**Goal: maintain a useful, attractive, current README for the loop-generative-models paper collection.**

The README is the main reading interface. The bot refreshes its collection
counts, taxonomy links, curated reading path, full grouped collection, recent
additions, and oversight reading list whenever it publishes metadata. Titles and
links come from the same records as the full bibliography. Existing prose outside the six marked
`LOOP-BOT` sections belongs to the curators and is preserved.

## Collection and publication

1. The existing Railway Discord bot reads posts in five configured research channels and their accessible active and archived threads.
2. It extracts canonical arXiv IDs, verifies identity against official metadata, and deduplicates versions and repeated mentions.
3. Explicit recurrent-depth matches and high-confidence mechanism matches can enter the list automatically. Other papers enter the review queue.
4. GitHub Actions fetches the public metadata, updates the data, indexes and README in one commit, and acknowledges publication.

Both stages run every 30 minutes. Hosting delays can extend delivery time.
The workflow also supports manual dispatch. Publication failures leave records
pending; a new run reconciles them with the latest repository contents. A
concurrent human commit causes a normal push rejection and retry, never a force push.

## Editorial rules

- Preserve existing records; do not overwrite human corrections with fetched metadata.
- Keep uncertain papers visibly separate from accepted ones.
- Never claim experimental reproduction based on inclusion in the list.
- Keep dates of addition separate from dates of publication.
- Use primary paper links. Non-arXiv reports require manual addition.
- Keep the reading map curated in `data/reading_map.json`; do not silently invent representative-paper rankings.
- Stop if README markers or reading-map references are invalid. This prevents a malformed update from replacing curator prose.
- Respect `data/excluded.json`; removing a rejected item from a list alone does not permanently exclude it.

The history boundary is the Discord epoch (2015-01-01), so accessible older
posts are included in the initial backfill. Each channel and thread has an
independent cursor. Archived public threads are paginated; private threads are
limited to those the bot can already access. The bot does not join or reopen
threads or change permissions. Discovery or scan errors are reported as incomplete
coverage. A scan is limited to 5,000 messages per channel or thread and 5,000
archived threads per archive type; hitting a limit is reported, never silently
treated as complete.

The collector does not rescan edits to old messages or infer paper titles from
images. Non-arXiv links require manual reconciliation. The [dated source audit](SOURCE_COVERAGE.md)
describes what was actually checked; a collection count is not a coverage metric.

The collector does not modify the Overleaf manuscript. Private messages, discussion text, channel IDs
and credentials never appear in this repository or in the classifier's input;
classification receives public titles and abstracts only.

## Reading groups and counts

`reading_group` records the primary reading topic of each survey reference.
These assignments follow its discussion context and include supporting papers;
they do not certify a paper's architecture. `family` records the mechanism assigned
by relevance screening. The README uses an explicit reading group first, then
the screened family, with an unclassified group as a visible fallback.

All accepted records appear exactly once in the full README catalog. Candidates
appear in a separate expandable group and are excluded from the main count.
The five taxonomy families coexist with supporting topics for foundations,
training, and evaluation. The `listed works` badge includes model reports and
background references imported from the survey; it is not a Discord collection count.

## Configuration and recovery

The repository Actions secret `LOOP_PAPERS_FEED_SECRET` must match Railway's
secret of the same name. `LOOP_PAPERS_FEED_URL` is a repository variable pointing
to the HTTPS `/loop-papers/feed` endpoint. GitHub writes use the workflow's
built-in token with `contents: write`; Railway holds no GitHub write credential.

Check **Actions → Update paper list** for a failed run. Check Railway logs for
`Loop papers scan complete` or `Loop papers publication acknowledged`. Metadata
failures retry; unusable classifier responses go to relevance review. To stop
updates, disable the workflow and set `LOOP_PAPERS_ENABLED=false` in Railway.

## Local validation

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
```

`scripts/update_papers.py` publishes when run with feed credentials and a writable
Git remote. Use the unit tests above for local checks without publishing.
