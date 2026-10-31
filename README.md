# AEO, GEO and SEO Field Guide

A free, beginner-friendly guide and checklist for SEO, AEO and GEO work.

- **SEO**: rank pages in search results.
- **AEO** (answer engine optimization): get a brand named, described correctly and cited in AI answers (ChatGPT, Google AI Overviews and AI Mode, Gemini, Perplexity, Claude, Copilot).
- **GEO** (generative engine optimization): a near-synonym of AEO. This guide treats all three as one practice. SEO is the base.

It goes from first look to long-term care: inspect a brand, suggest fixes, build them, keep them healthy, and grow. It also shows how an expert thinks at each step, and which tools experts use and when.

## Read it

| File | What it is |
|---|---|
| [`out/guide.html`](out/guide.html), [`out/guide.pdf`](out/guide.pdf), [`out/guide.md`](out/guide.md) | The Field Guide (11 parts: big picture, how search and AI answers work, how experts think, the job step by step, client types, tools, freelancing, learning path, templates, glossary, sources) |
| [`out/checklist.html`](out/checklist.html), [`out/checklist.pdf`](out/checklist.pdf), [`out/checklist.md`](out/checklist.md) | The Practitioner Checklist (179 tasks, 9 phases). In the HTML, type a client name: ticks save per client in your browser. Export CSV works |

The HTML files work offline. Download them and open them in a browser.

## Change it

| File | What it is |
|---|---|
| `src/guide/*.md` | Guide source. Edit here |
| `src/checklist.yaml` | Checklist source. Edit here |
| `build.py` | Rebuilds `out/` |

Rebuild (needs [uv](https://docs.astral.sh/uv/)):

```powershell
uv run --no-project --with markdown --with pyyaml python build.py
```

Print the PDFs with Edge (Windows):

```powershell
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --print-to-pdf="$PWD\out\guide.pdf" "file:///$($PWD -replace '\\','/')/out/guide.html"
& "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --headless=new --no-pdf-header-footer --print-to-pdf="$PWD\out\checklist.pdf" "file:///$($PWD -replace '\\','/')/out/checklist.html"
```

## Sync (Windows)

- `start.bat`: get the latest version before you work.
- `sync.bat`: save your changes and upload them.

## Keep it current

AI search changes month to month. The figures in this guide are each company's own findings, cited to their owner. Check them again before you use them with a client. Version 1: 31 Oct 2026.

## Licence

The guide and checklist text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You can use, share and change it, also for paid work. Give credit and link back here.

`build.py`, `start.bat` and `sync.bat`: MIT licence.

Quotes, figures and names from other people's work stay theirs. See Part 11 (Sources) in the guide.
