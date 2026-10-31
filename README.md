# AEO, GEO and SEO Field Guide (Rey's own)

Rey's personal guide and checklist for doing SEO, AEO and GEO work as an independent expert. Kept apart from Buzz Insider's repo on purpose: Buzz work stays with Buzz (contract, 23 Oct 2026); this guide is Rey's own learning, built from public courses and books.

## Files

| File | What it is |
|---|---|
| `out/guide.html`, `out/guide.pdf`, `out/guide.md` | The Field Guide (11 parts: big picture, how search and AI answers work, how experts think, the job step by step, client types, tools, freelancing, learning path, templates, glossary, sources) |
| `out/checklist.html`, `out/checklist.pdf`, `out/checklist.md` | The Practitioner Checklist (179 tasks, 9 phases). In the HTML, type a client name: ticks save per client in the browser. Export CSV works |
| `src/guide/*.md` | Guide source. Edit here |
| `src/checklist.yaml` | Checklist source. Edit here |
| `build.py` | Rebuilds `out/` |

## Rebuild

```powershell
uv run --no-project --with markdown --with pyyaml python build.py
```

PDFs: print with Edge.

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --print-to-pdf="C:\Projects\aeo-expert-guide\out\guide.pdf" "file:///C:/Projects/aeo-expert-guide/out/guide.html"
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --print-to-pdf="C:\Projects\aeo-expert-guide\out\checklist.pdf" "file:///C:/Projects/aeo-expert-guide/out/checklist.html"
```

## Keep it current

AI search changes month to month. Recheck figures (they are each company's own findings) before using them with a client. Version 1: 31 Oct 2026.
