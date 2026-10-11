#!/usr/bin/env python3
"""
build_status_dashboard.py

Turn a `LAUNCH_STATUS.md` tracking table into a single, self-contained HTML
dashboard — no CDN, no dependencies, safe to open offline or email to the owner.

It reads the pipe table defined by the skill (Phase 6), for example::

    venue | type | mode | submitted_at | confirm_id | live_url | link_rel | robots | status | owner_action_needed

and renders:

  * summary stat cards (total, live, pending, blocked, todo),
  * unique referring domains across live placements,
  * an indexability split (live+indexed vs live+noindex),
  * the list of `owner_action_needed` items (one human step each),
  * a status distribution chart, and
  * a searchable / filterable table of every row.

Usage
-----
    python3 build_status_dashboard.py --input LAUNCH_STATUS.md --out LAUNCH_DASHBOARD.html
    python3 build_status_dashboard.py --input LAUNCH_STATUS.md \
        --title "Acme launch — citation status"

Column names are matched loosely, so `live_url`, `Live URL` and `liveurl` all
work, and extra columns are shown in the table without breaking anything.
"""
from __future__ import annotations

import argparse
import html
import re
from collections import Counter

# Common multi-part public suffixes for a "referring domain" approximation.
MULTI_SUFFIXES = {
    "co.uk", "org.uk", "gov.uk", "ac.uk", "co.jp", "com.au", "co.nz", "co.in",
    "com.br", "com.mx", "co.za", "com.cn", "github.io", "pages.dev", "workers.dev",
    "web.app", "firebaseapp.com", "vercel.app", "netlify.app", "s3.amazonaws.com",
    "storage.googleapis.com", "archive.org", "blogspot.com", "wordpress.com",
}


def norm(header: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", header.strip().lower()).strip("_")


def referring_domain(url: str) -> str:
    """Approximate the registrable root domain (eTLD+1) of a URL."""
    url = (url or "").strip()
    if not url:
        return ""
    m = re.match(r"^[a-zA-Z]+://([^/]+)", url)
    host = (m.group(1) if m else url.split("/")[0]).split(":")[0].lower()
    if not host:
        return ""
    for suffix in sorted(MULTI_SUFFIXES, key=len, reverse=True):
        if host == suffix or host.endswith("." + suffix):
            labels = suffix.split(".")
            return ".".join(host.split(".")[-(len(labels) + 1):])
    parts = host.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def parse_status(md_text: str):
    """Return (headers, rows) from the first pipe table that has a status column."""
    headers: list[str] = []
    rows: list[dict] = []
    started = False
    for raw in md_text.splitlines():
        line = raw.strip()
        if "|" not in line:
            if started and rows:
                break
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not started:
            if any("venue" in norm(c) for c in cells) and any("status" in norm(c) for c in cells):
                headers = cells
                started = True
            continue
        if all(set(c) <= {"-", ":", " "} for c in cells):
            continue  # separator row
        row = {}
        for i, h in enumerate(headers):
            row[norm(h)] = cells[i] if i < len(cells) else ""
        if any(v for v in row.values()):
            rows.append(row)
    return headers, rows


def cell(row: dict, *keys: str) -> str:
    for k in keys:
        if k in row and row[k]:
            return row[k]
    return ""


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
  :root{--bg:#f6f7f9;--card:#fff;--line:#e9e9ee;--ink:#14141a;--muted:#71717a;
    --accent:#4f46e5;--accent2:#0ea5e9;--ok:#0f9d58;--warn:#d97706;--bad:#dc2626;
    --radius:16px;--shadow:0 1px 2px rgba(15,15,20,.04),0 10px 30px rgba(15,15,20,.05);}
  *{box-sizing:border-box}html,body{margin:0}
  body{background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased;
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .wrap{max-width:1140px;margin:0 auto;padding:0 22px}
  header{padding:54px 0 28px;background:radial-gradient(880px 320px at 12% -25%,#eef2ff 0,transparent 60%),radial-gradient(720px 300px at 96% -35%,#ecfeff 0,transparent 55%)}
  .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.09em;
    text-transform:uppercase;color:var(--accent);background:#fff;border:1px solid var(--line);padding:6px 12px;border-radius:999px;box-shadow:var(--shadow)}
  .dot{width:7px;height:7px;border-radius:999px;background:var(--ok)}
  h1{font-size:clamp(26px,4.4vw,42px);line-height:1.06;letter-spacing:-.028em;margin:18px 0 12px;font-weight:760}
  .sub{color:var(--muted);max-width:800px;font-size:16px;margin:0}
  main{padding:6px 0 70px}
  .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin:8px 0 18px}
  .stat{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:16px;box-shadow:var(--shadow)}
  .stat .k{font-size:12.5px;color:var(--muted);font-weight:650}
  .stat .v{font-size:28px;font-weight:750;letter-spacing:-.02em;margin-top:6px}
  .stat .d{font-size:12.5px;color:var(--muted);margin-top:2px}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow)}
  .card h2{margin:0 0 4px;font-size:15px;font-weight:700}
  .cap{color:var(--muted);font-size:13px;margin:0 0 14px}
  .bars{display:flex;flex-direction:column;gap:12px}
  .bar{display:grid;grid-template-columns:150px 1fr 44px;align-items:center;gap:12px;font-size:13.5px}
  .bar .lbl{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .track{background:#f1f1f4;border-radius:999px;height:9px}
  .fill{height:9px;border-radius:999px;background:linear-gradient(90deg,var(--accent),var(--accent2))}
  .bar .val{text-align:right;color:var(--muted);font-weight:700}
  .actions{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px}
  .actions li{display:flex;gap:10px;align-items:flex-start;font-size:14px;color:#3f3f46}
  .doti{flex:0 0 auto;width:22px;height:22px;border-radius:7px;display:grid;place-items:center;background:#eef2ff;color:var(--accent);font-size:12px;font-weight:800}
  .toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:14px}
  #q{flex:1 1 240px;min-width:200px;font:inherit;background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 13px;outline:none}
  #q:focus{border-color:#c7d2fe;box-shadow:0 0 0 3px rgba(79,70,229,.12)}
  .chips{display:flex;gap:6px;flex-wrap:wrap}
  .chip{border:1px solid var(--line);background:#fff;color:var(--muted);font-weight:650;font-size:13px;padding:8px 13px;border-radius:999px;cursor:pointer}
  .chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
  .count{margin-left:auto;color:var(--muted);font-size:13px;font-weight:650}
  .tablewrap{overflow:auto;border:1px solid var(--line);border-radius:12px}
  table{width:100%;border-collapse:separate;border-spacing:0;font-size:13.5px}
  thead th{position:sticky;top:0;background:#fbfbfc;z-index:1;text-align:left;font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:750;padding:11px 13px;border-bottom:1px solid var(--line);white-space:nowrap}
  tbody td{padding:10px 13px;border-bottom:1px solid #f4f4f6;vertical-align:top}
  tbody tr:hover{background:#fafafb}
  .b{display:inline-block;font-size:11.5px;font-weight:750;padding:3px 9px;border-radius:999px;background:#f3f3f5;color:#52525b}
  .b.live{background:#e8f6ef;color:#0b6b3f}
  .b.live_noindex{background:#fef3c7;color:#92400e}
  .b.pending_review,.b.submitted{background:#e0e7ff;color:#3730a3}
  .b.blocked{background:#fee2e2;color:#991b1b}
  .b.removed{background:#e4e4e7;color:#3f3f46;text-decoration:line-through}
  a{color:var(--accent)}
  .empty{padding:40px;text-align:center;color:var(--muted)}
  footer{padding:26px 0 60px;color:var(--muted);font-size:13px;max-width:820px}
  @media (max-width:880px){.grid2{grid-template-columns:1fr}}
</style>
</head>
<body>
<header><div class="wrap">
  <span class="eyebrow"><span class="dot"></span> Launch status dashboard</span>
  <h1>__TITLE__</h1>
  <p class="sub">Placement tracking, referring-domain coverage and owner action items · <span id="date"></span></p>
</div></header>
<main class="wrap">
  <section class="stats" id="stats"></section>
  <section class="grid2">
    <div class="card"><h2>Status distribution</h2><p class="cap">Every venue by current status</p><div class="bars" id="chartStatus"></div></div>
    <div class="card"><h2>Owner action needed</h2><p class="cap">One clear human step each</p><div id="actions"></div></div>
  </section>
  <section class="card" style="margin-bottom:16px">
    <h2>Placements</h2>
    <div class="toolbar">
      <input id="q" placeholder="Search venue, domain or status…">
      <div class="chips" id="chips"></div>
      <span class="count" id="count"></span>
    </div>
    <div class="tablewrap"><table>
      <thead id="thead"></thead>
      <tbody id="rows"></tbody>
    </table></div>
  </section>
  <footer>Generated <span id="date2"></span> · Rendered from the campaign's <code>LAUNCH_STATUS.md</code>. Never treat a <code>submitted</code> row as a success — verify HTTP 200, both URLs and indexability first.</footer>
</main>
<script>
const HEADERS = __HEADERS__;
const ROWS = __ROWS__;
const $ = s => document.querySelector(s);
const nk = h => h.toLowerCase().replace(/[^a-z0-9]+/g,'_').replace(/^_|_$/g,'');
const KEYS = HEADERS.map(nk);
const norm = r => { const o={}; HEADERS.forEach((h,i)=>{ o[nk(h)] = r[i]||''; }); return o; };
const pick = (o,...ks) => { for(const k of ks){ if(o[k]) return o[k]; } return ''; };
const OBJS = ROWS.map(norm);

function refDomain(url){
  const m = /^[a-zA-Z]+:\/\/([^\/]+)/.exec(url||'');
  const host = m ? m[1] : (url||'').split('/')[0];
  const parts = host.split('.');
  if(parts.length<=2) return host;
  const multi = ['co.uk','org.uk','gov.uk','ac.uk','com.au','co.nz','com.br','github.io','pages.dev','workers.dev','web.app','vercel.app','netlify.app','blogspot.com','wordpress.com'];
  const two = parts.slice(-2).join('.');
  if(multi.includes(two)) return parts.slice(-3).join('.');
  return two;
}

const statusOf = o => pick(o,'status') || 'todo';
const urlOf = o => pick(o,'live_url','liveurl','url','link');
const actionOf = o => pick(o,'owner_action_needed','owner_action','action');

function renderStats(){
  const c = {}; OBJS.forEach(o=>{const s=statusOf(o); c[s]=(c[s]||0)+1;});
  const live = c['live']||0, noidx = c['live_noindex']||0;
  const rds = new Set(OBJS.map(urlOf).filter(Boolean).map(refDomain).filter(Boolean));
  const actions = OBJS.filter(o=>actionOf(o)).length;
  const cards = [
    ['Total venues', ROWS.length, 'in the tracker'],
    ['Live', live, live+noidx+' confirmed live'],
    ['Unique referring domains', rds.size, 'distinct roots linked'],
    ['Pending review', c['pending_review']||0, 'awaiting moderation'],
    ['Blocked', c['blocked']||0, 'need a different route'],
    ['Owner actions', actions, 'human steps open'],
  ];
  $('#stats').innerHTML = cards.map(([k,v,d])=>`<div class="stat"><div class="k">${k}</div><div class="v">${v}</div><div class="d">${d}</div></div>`).join('');
  return c;
}

function renderChart(c){
  const order = ['live','live_noindex','pending_review','submitted','todo','blocked','removed'];
  const entries = order.filter(k=>c[k]).map(k=>[k,c[k]]).concat(Object.keys(c).filter(k=>!order.includes(k)).map(k=>[k,c[k]]));
  const max = Math.max(1,...entries.map(e=>e[1]));
  $('#chartStatus').innerHTML = entries.length ? entries.map(([k,v])=>
    `<div class="bar"><div class="lbl">${k}</div><div class="track"><div class="fill" style="width:${(v/max*100).toFixed(1)}%"></div></div><div class="val">${v}</div></div>`).join('')
    : '<p class="cap">No rows yet.</p>';
}

function renderActions(){
  const items = OBJS.filter(o=>actionOf(o));
  $('#actions').innerHTML = items.length ? '<div class="taglist">' + items.map(r=>
    `<div style="padding:8px 0;border-bottom:1px solid #f4f4f6"><b>${pick(r,'venue')||'—'}</b><div class="cap" style="margin:2px 0 0">${actionOf(r)}</div></div>`).join('') + '</div>'
    : '<p class="cap">No owner actions open.</p>';
}

let activeStatus = 'all';
function renderChips(c){
  const sts = ['all',...Object.keys(c)];
  $('#chips').innerHTML = sts.map(s=>`<button class="chip ${s===activeStatus?'on':''}" data-s="${s}">${s==='all'?'All':s}${s==='all'?'':' ('+c[s]+')'}</button>`).join('');
  $('#chips').querySelectorAll('.chip').forEach(b=>b.onclick=()=>{activeStatus=b.dataset.s;renderChips(c);renderTable();});
}

function renderTable(){
  const q = $('#q').value.trim().toLowerCase();
  const visible = OBJS.filter(o=>
    (activeStatus==='all' || statusOf(o)===activeStatus) &&
    (!q || HEADERS.some(h=>String(o[nk(h)]||'').toLowerCase().includes(q)))
  );
  $('#count').textContent = visible.length + ' of ' + ROWS.length + ' shown';
  $('#rows').innerHTML = visible.map(o=>'<tr>' + HEADERS.map(h=>{
    const key = nk(h); const v = o[key]||'';
    if(key==='status') return `<td><span class="b ${v}">${v||'todo'}</span></td>`;
    if((key==='live_url'||key==='url') && v) return `<td><a href="${v}" target="_blank" rel="noopener">${refDomain(v)}</a></td>`;
    return `<td>${v}</td>`;
  }).join('') + '</tr>').join('')
    || `<tr><td colspan="${HEADERS.length||1}" class="empty">No rows match.</td></tr>`;
}

function init(){
  const dt = new Date().toISOString().slice(0,10);
  $('#date').textContent = dt; $('#date2').textContent = dt;
  $('#thead').innerHTML = '<tr>' + HEADERS.map(h=>`<th>${h}</th>`).join('') + '</tr>';
  const c = renderStats(); renderChart(c); renderActions(); renderChips(c);
  $('#q').oninput=renderTable;
  renderTable();
}
init();
</script>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", default="LAUNCH_STATUS.md")
    ap.add_argument("--out", default="LAUNCH_DASHBOARD.html")
    ap.add_argument("--title", default="Launch status dashboard")
    args = ap.parse_args()

    text = open(args.input, encoding="utf-8").read()
    headers, rows = parse_status(text)
    if not headers:
        raise SystemExit("no status table found (need a pipe table with 'venue' and 'status' columns)")

    import json
    headers_js = json.dumps(headers)
    rows_js = json.dumps([[r.get(norm(h), "") for h in headers] for r in rows]).replace("</", "<\\/")

    out = (TEMPLATE
           .replace("__TITLE__", html.escape(args.title))
           .replace("__HEADERS__", headers_js)
           .replace("__ROWS__", rows_js))
    open(args.out, "w", encoding="utf-8").write(out)
    print(f"wrote {args.out} ({len(out):,} bytes, {len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
