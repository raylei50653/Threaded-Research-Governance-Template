# scripts/tools (phase 2)

v1 of this template is **convention-first**. Automated checkers are intentionally deferred.

## Planned

| Script | Role | Severity |
|:--|:--|:--|
| `check_doc_structure.py` | research notes not referenced by owning README | warn-only |
| `check_doc_links.py` | broken relative links | hard (optional) |
| `check_doc_stale_paths.py` | phantom paths in entry docs | hard (optional) |

## Manual until then

Use the human checklist in [docs/DOC_MAINTENANCE.md](../../docs/DOC_MAINTENANCE.md):

```text
□ new research has status markers
□ owning README index row same PR
□ promotion path if numbers are citable
□ no phantom links
□ WIP=1 still holds
```
