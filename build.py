"""Build the guide and checklist (Markdown, HTML) from src/. Print PDFs with Edge afterwards.

Usage: uv run --with markdown --with pyyaml python build.py [src_dir] [out_dir]
"""
import html
import json
import re
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "src"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "out"

CSS = """
:root{--ink:#1d2433;--muted:#5b6475;--line:#d9dee7;--bg:#f6f7f9;--accent:#2f5bd3;--ok:#1f7a4d}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{font:16px/1.6 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--ink);margin:0;background:#fff}
a{color:var(--accent)}
.wrap{display:grid;grid-template-columns:280px minmax(0,1fr);max-width:1280px;margin:0 auto}
nav.toc{position:sticky;top:0;height:100vh;overflow:auto;padding:24px 16px;border-right:1px solid var(--line);background:var(--bg);font-size:14px}
nav.toc ul{list-style:none;padding-left:12px;margin:4px 0}nav.toc>ul{padding-left:0}
nav.toc a{color:var(--ink);text-decoration:none}nav.toc a:hover{color:var(--accent)}
main{padding:32px 40px 80px;min-width:0}
h1{font-size:30px;line-height:1.2;margin:0 0 8px}h2{font-size:24px;margin:48px 0 8px;padding-top:8px;border-top:2px solid var(--line)}
h3{font-size:19px;margin:30px 0 6px}h4{font-size:16px;margin:22px 0 4px}
table{border-collapse:collapse;width:100%;margin:12px 0 18px;font-size:14.5px}
th,td{text-align:left;vertical-align:top;padding:7px 9px;border-bottom:1px solid var(--line)}
th{background:var(--bg);font-weight:600}
code{background:var(--bg);padding:1px 5px;border-radius:4px;font-size:13.5px}
blockquote{border-left:4px solid var(--line);margin:12px 0;padding:4px 14px;color:var(--muted)}
hr{border:0;border-top:1px solid var(--line);margin:32px 0}
.meta{color:var(--muted);font-size:14px}
@media (max-width:900px){.wrap{display:block}nav.toc{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line)}main{padding:20px}}
@media print{nav.toc{display:none}.wrap{display:block}main{padding:0}body{font-size:11.5px}h2{break-before:page;border-top:0}
table{font-size:10.5px}tr,h3,h4{break-inside:avoid}a{color:var(--ink);text-decoration:none}}
"""

CL_CSS = """
:root{--ink:#1d2433;--muted:#5b6475;--line:#d9dee7;--bg:#f6f7f9;--accent:#2f5bd3}
*{box-sizing:border-box}body{font:15px/1.5 -apple-system,Segoe UI,Roboto,Arial,sans-serif;color:var(--ink);margin:0}
header{padding:24px 32px 12px;border-bottom:1px solid var(--line)}h1{font-size:24px;margin:0 0 6px}.sub{color:var(--muted);margin:0}
.bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;padding:10px 32px;background:var(--bg);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:2}
.bar input,.bar select{padding:6px 8px;border:1px solid var(--line);border-radius:6px}.bar input[type=text]{min-width:220px}
.bar button{padding:6px 10px;border:1px solid var(--line);background:#fff;border-radius:6px;cursor:pointer}
.prog{font-weight:600}main{padding:4px 32px 48px}
h2{font-size:19px;margin:28px 0 2px}.intro{color:var(--muted);margin:0 0 6px}h3{font-size:15px;margin:16px 0 4px;color:var(--accent)}
table{border-collapse:collapse;width:100%;table-layout:fixed}th,td{text-align:left;vertical-align:top;padding:6px 7px;border-bottom:1px solid var(--line);overflow-wrap:anywhere}
th{font-size:12px;text-transform:uppercase;letter-spacing:.03em;color:var(--muted)}td.id{white-space:nowrap;color:var(--muted)}td.box{width:26px}
td input.f,td select.f{width:100%;border:1px solid transparent;background:transparent;font:inherit;padding:2px 4px}
td input.f:hover,td input.f:focus,td select.f:hover{border-color:var(--line);background:#fff}
tr.done td{opacity:.5}tr.done td.task{text-decoration:line-through}
.why{color:var(--muted)}footer{padding:16px 32px;color:var(--muted);font-size:13px;border-top:1px solid var(--line)}
@media print{.bar{display:none}header,main,footer{padding-left:0;padding-right:0}body{font-size:10.5px}h2{break-after:avoid}tr{break-inside:avoid}
td input.f,td select.f{border:0;appearance:none}}
"""


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build_guide() -> None:
    parts = sorted((SRC / "guide").glob("*.md"))
    text = "\n\n".join(p.read_text(encoding="utf-8") for p in parts)
    (OUT / "guide.md").write_text(text, encoding="utf-8")
    md = markdown.Markdown(extensions=["tables", "toc", "sane_lists"], extension_configs={"toc": {"toc_depth": "2-3", "slugify": lambda v, s: slug(v)}})
    body = md.convert(text)
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    page = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
        f"<div class='wrap'><nav class='toc'><b>Contents</b>{md.toc}</nav><main>{body}</main></div></body></html>"
    )
    (OUT / "guide.html").write_text(page, encoding="utf-8")


def load_checklist() -> dict:
    return yaml.safe_load((SRC / "checklist.yaml").read_text(encoding="utf-8"))


def build_checklist_md(data: dict) -> str:
    cols = data.get("columns", [["task", "Task"], ["why", "Why"], ["how", "How"], ["done", "Done when"]])
    lines = [f"# {data['title']}", "", data.get("subtitle", ""), ""]
    for ph in data["phases"]:
        lines += [f"## {ph['id']}. {ph['title']}", "", ph.get("intro", ""), ""]
        for g in ph["groups"]:
            lines += [f"### {g['title']}", "", "| # | " + " | ".join(c[1] for c in cols) + " |", "|---|" + "---|" * len(cols)]
            for it in g["items"]:
                lines.append(f"| {it['id']} | " + " | ".join(str(it.get(c[0], "")).replace("|", "/") for c in cols) + " |")
            lines.append("")
    if data.get("footer"):
        lines += ["---", "", data["footer"], ""]
    return "\n".join(lines)


def build_checklist_html(data: dict) -> str:
    e = html.escape
    cols = data.get("columns", [["task", "Task"], ["why", "Why"], ["how", "How"], ["done", "Done when"]])
    editable = data.get("editable", [])
    statuses = data.get("statuses", [])
    key = slug(data["title"])
    total = sum(len(g["items"]) for ph in data["phases"] for g in ph["groups"])
    out = [
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>",
        f"<title>{e(data['title'])}</title><style>{CL_CSS}</style></head><body>",
        f"<header><h1>{e(data['title'])}</h1><p class='sub'>{e(data.get('subtitle', ''))} {total} items.</p></header>",
        f"<div class='bar'><label>{e(data.get('client_label', 'Client'))}: <input id='who' type='text' placeholder='Type a name; ticks and edits save per name in this browser'></label>",
        "<span class='prog' id='prog'></span><label>Phase: <select id='ph'><option value=''>All</option>",
    ]
    out += [f"<option value='{e(ph['id'])}'>{e(ph['id'])}. {e(ph['title'])}</option>" for ph in data["phases"]]
    out.append("</select></label><button onclick='hideDone()'>Hide done</button><button onclick='exportCsv()'>Export CSV</button><button onclick='window.print()'>Print or save PDF</button></div><main>")
    for ph in data["phases"]:
        out.append(f"<section data-ph='{e(ph['id'])}'><h2>{e(ph['id'])}. {e(ph['title'])}</h2><p class='intro'>{e(ph.get('intro', ''))}</p>")
        for g in ph["groups"]:
            widths = data.get("widths", ["22%", "22%", "30%", "26%"])
            cg = "<colgroup><col style='width:30px'><col style='width:52px'>" + "".join(f"<col style='width:{w}'>" for w in widths) + "</colgroup>"
            out.append(f"<h3>{e(g['title'])}</h3><table>{cg}<thead><tr><th></th><th>#</th>")
            out += [f"<th>{e(c[1])}</th>" for c in cols]
            out += [f"<th>{e(f.capitalize())}</th>" for f in editable]
            out.append("</tr></thead><tbody>")
            for it in g["items"]:
                iid = e(str(it["id"]))
                row = [f"<tr data-id='{iid}'><td class='box'><input class='c' type='checkbox' aria-label='Done {iid}'></td><td class='id'>{iid}</td>"]
                for c in cols:
                    cls = "task" if c[0] == "task" else ("why" if c[0] == "why" else "")
                    row.append(f"<td class='{cls}'>{e(str(it.get(c[0], '')))}</td>")
                for f in editable:
                    val = e(str(it.get(f, "")))
                    if f == "status" and statuses:
                        opts = "".join(f"<option{' selected' if s == it.get(f) else ''}>{e(s)}</option>" for s in statuses)
                        row.append(f"<td><select class='f' data-f='{f}' data-default='{val}'>{opts}</select></td>")
                    else:
                        row.append(f"<td><input class='f' data-f='{f}' data-default='{val}' value='{val}'></td>")
                row.append("</tr>")
                out.append("".join(row))
            out.append("</tbody></table>")
        out.append("</section>")
    out.append(f"</main><footer>{e(data.get('footer', ''))}</footer>")
    js = """
const K='KEY:';const who=()=>K+(document.getElementById('who').value.trim().toLowerCase()||'default');
function load(){const s=JSON.parse(localStorage.getItem(who())||'{}');document.querySelectorAll('tr[data-id]').forEach(r=>{const d=s[r.dataset.id]||{};const b=r.querySelector('input.c');b.checked=!!d.done;r.classList.toggle('done',b.checked);r.querySelectorAll('.f').forEach(f=>{f.value=(d[f.dataset.f]!==undefined)?d[f.dataset.f]:f.dataset.default})});prog()}
function save(){const s={};document.querySelectorAll('tr[data-id]').forEach(r=>{const d={};const b=r.querySelector('input.c');if(b.checked)d.done=1;r.querySelectorAll('.f').forEach(f=>{if(f.value!==f.dataset.default)d[f.dataset.f]=f.value});if(Object.keys(d).length)s[r.dataset.id]=d});localStorage.setItem(who(),JSON.stringify(s));prog()}
function prog(){const a=document.querySelectorAll('input.c'),n=[...a].filter(b=>b.checked).length;document.getElementById('prog').textContent=n+' of '+a.length+' done'}
let hid=false;function hideDone(){hid=!hid;document.querySelectorAll('tr.done').forEach(r=>r.style.display=hid?'none':'')}
function exportCsv(){const rows=[['id','done'].concat([...document.querySelectorAll('thead')[0].querySelectorAll('th')].slice(2).map(t=>t.textContent))];document.querySelectorAll('tr[data-id]').forEach(r=>{const c=[r.dataset.id,r.querySelector('input.c').checked?'yes':''];r.querySelectorAll('td').forEach((td,i)=>{if(i<2)return;const f=td.querySelector('.f');c.push(f?f.value:td.textContent)});rows.push(c)});const csv=rows.map(r=>r.map(v=>'"'+String(v).replace(/"/g,'""')+'"').join(',')).join('\\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv'}));a.download='checklist.csv';a.click()}
document.addEventListener('change',ev=>{if(ev.target.matches('input.c'))ev.target.closest('tr').classList.toggle('done',ev.target.checked);if(ev.target.matches('input.c,.f'))save()});
document.addEventListener('input',ev=>{if(ev.target.matches('input.f'))save()});
document.getElementById('ph').addEventListener('change',ev=>{document.querySelectorAll('section[data-ph]').forEach(s=>s.style.display=(!ev.target.value||s.dataset.ph===ev.target.value)?'':'none')});
const w=document.getElementById('who');w.value=localStorage.getItem(K+'last')||'';w.addEventListener('input',()=>{localStorage.setItem(K+'last',w.value)});w.addEventListener('change',load);load();
""".replace("KEY", key)
    out.append(f"<script>{js}</script></body></html>")
    return "".join(out)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if (SRC / "guide").is_dir():
        build_guide()
    data = load_checklist()
    (OUT / "checklist.md").write_text(build_checklist_md(data), encoding="utf-8")
    (OUT / "checklist.html").write_text(build_checklist_html(data), encoding="utf-8")
    items = sum(len(g["items"]) for ph in data["phases"] for g in ph["groups"])
    print(json.dumps({"out": str(OUT), "checklist_items": items}))


if __name__ == "__main__":
    main()
