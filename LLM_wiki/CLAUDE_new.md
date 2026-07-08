# Knowledge Base Schema

## What This Is
A personal knowledge base in the OpenKB layout (https://github.com/VectifyAI/OpenKB), following Google's Open Knowledge Format (OKF): markdown pages with YAML frontmatter, linked into a knowledge graph, with `index.md` hierarchy and `log.md` history.

## How It's Organized
- raw/ contains unprocessed source material. It is IMMUTABLE: never modify, delete, move, or rename anything in raw/. The wiki's provenance depends on every cited raw file staying exactly where it is; a deleted raw source makes its wiki article impossible to rebuild or re-verify. The only exception ever permitted was a one-time, user-authorized removal of clearly non-knowledge material (mail archives, app state, empty folders); do not treat that as license to prune raw/ again. If raw/ seems to contain junk, propose it and wait for explicit approval, never delete on your own initiative.
- wiki/ contains the organized wiki. AI maintains this entirely.
  - wiki/concepts/ — topic pages (one .md per topic)
  - wiki/entities/ — people, organizations, places, products
  - wiki/explorations/ — saved query results and durable analyses
  - wiki/index.md + per-folder index.md — hierarchy, one line per page
  - wiki/log.md — append-only change log
  - wiki/AGENTS.md — detailed governance rules for maintaining the wiki (read it before editing wiki content)
- outputs/ contains generated reports, answers, and analyses (OpenKB's generated-artifacts directory; kept under this name). It is a working area, not curated knowledge: material there may be stale, superseded, or unreviewed. (`output` is a hidden compatibility symlink to outputs/, needed because OpenKB hardcodes that path. Keep it; never create a real output/ directory.)
- .openkb/ contains OpenKB configuration.

## Source Discipline
- Knowledge lookups, research, and content for new deliverables draw on wiki/ (curated) and raw/ (immutable sources) only.
- Never read, cite, or reuse material from outputs/ on your own initiative — not as examples, prior art, or reference. Work with an outputs/ subfolder only when the user explicitly names it for the current task.
- Writing new deliverables into outputs/ (each in its own subfolder) remains the normal workflow.

## Wiki Rules (OKF)
- Every page carries YAML frontmatter: `type` is required (Concept, Organization, Person, Place, Product, Exploration, Index); title, description, tags, timestamp are expected; `resource` is optional.
- Every page starts (after frontmatter) with a one-paragraph summary.
- Article bodies link related pages with folder-qualified wikilinks ([[concepts/topic]], [[entities/name]]); index files use relative markdown links.
- Maintain the index.md files: every page listed once with a one-line description.
- When new raw sources are added, update the relevant wiki articles and refresh their `timestamp`.

## Answering Knowledge Questions
- Two engines exist, and the user chooses per question: `/kb <question>` = Claude answers directly from the curated wiki; `/openkb <question>` = the OpenKB query pipeline (Codex LLM) answers, returned verbatim.
- Plain questions without a slash command default to Claude answering per the /kb rules (grounded in wiki/, sources cited).
- Never route a question through `openkb query` on your own initiative; only via /openkb or when the user explicitly asks for the OpenKB engine.

## Change Log
- Maintain `wiki/log.md` — a chronological record of wiki changes so recent activity is easy to see.
- Append a new entry whenever wiki files are created, updated, split, renamed, or deleted (including during reindex runs).
- Entry format: `## YYYY-MM-DD` header (group multiple edits on the same day); beneath it, one bullet per change: what changed + one-line why/trigger. Keep bullets terse — the wiki files themselves are the detail.
- Newest entries go at the top of `log.md`. Only append; never rewrite historical entries.
- If the log gets long (~500 lines), archive older entries to `wiki/log-archive.md` grouped by year.
