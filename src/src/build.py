#!/usr/bin/env python3
"""Build the LDTS weekly slide decks (reveal.js, self-contained + CDN-enhanced)."""

import html as _html
import os
import re

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "decks")

AUTHOR = "Rui Maranhão"
COURSE = "LDTS · L.EIC014 · FEUP"
YEAR = "2026/2027"
REVEAL = "5.1.0"
HLJS = "11.9.0"

# --------------------------------------------------------------------------
# slide helpers
# --------------------------------------------------------------------------


def _notes(n):
    if not n:
        return ""
    return '<aside class="notes">%s</aside>' % n


def big(text, sub=None, notes=None):
    """One idea. Huge type. The backbone of the deck."""
    s = '<section class="s-big">'
    s += "<h2>%s</h2>" % text
    if sub:
        s += '<p class="sub">%s</p>' % sub
    return s + _notes(notes) + "</section>"


def q(text, sub=None, notes=None):
    """A Socratic question slide."""
    s = '<section class="s-q"><h2>%s</h2>' % text
    if sub:
        s += '<p class="sub">%s</p>' % sub
    return s + _notes(notes) + "</section>"


def part(kicker, text, notes=None):
    """Section divider."""
    return (
        '<section class="s-part"><p class="kicker">%s</p><h2>%s</h2>%s</section>'
        % (kicker, text, _notes(notes))
    )


def bullets(title, items, kicker=None, notes=None, tight=False):
    s = '<section class="s-list%s">' % (" tight" if tight else "")
    if kicker:
        s += '<p class="kicker">%s</p>' % kicker
    s += "<h3>%s</h3><ul>" % title
    for it in items:
        if isinstance(it, tuple):
            s += "<li>%s<ul>%s</ul></li>" % (
                it[0],
                "".join("<li>%s</li>" % x for x in it[1]),
            )
        else:
            s += "<li>%s</li>" % it
    s += "</ul>"
    return s + _notes(notes) + "</section>"


def code(title, lang, src, caption=None, notes=None, kicker=None):
    src = _html.escape(src.strip("\n").rstrip())
    s = '<section class="s-code">'
    if kicker:
        s += '<p class="kicker">%s</p>' % kicker
    if title:
        s += "<h3>%s</h3>" % title
    s += '<pre><code class="language-%s" data-trim data-noescape>%s</code></pre>' % (
        lang,
        src,
    )
    if caption:
        s += '<p class="cap">%s</p>' % caption
    return s + _notes(notes) + "</section>"


def two(title, left_h, left, right_h, right, notes=None, kicker=None):
    s = '<section class="s-two">'
    if kicker:
        s += '<p class="kicker">%s</p>' % kicker
    if title:
        s += "<h3>%s</h3>" % title
    s += (
        '<div class="cols"><div class="col"><h4>%s</h4>%s</div>'
        '<div class="col"><h4>%s</h4>%s</div></div>' % (left_h, left, right_h, right)
    )
    return s + _notes(notes) + "</section>"


def table(title, headers, rows, notes=None, kicker=None):
    # long tables step down a size so they still fit one canvas
    s = '<section class="s-table%s">' % (" dense" if len(rows) >= 9 else "")
    if kicker:
        s += '<p class="kicker">%s</p>' % kicker
    if title:
        s += "<h3>%s</h3>" % title
    s += '<div class="tw"><table><thead><tr>'
    s += "".join("<th>%s</th>" % h for h in headers)
    s += "</tr></thead><tbody>"
    for r in rows:
        s += "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
    s += "</tbody></table></div>"
    return s + _notes(notes) + "</section>"


def svg(title, body, caption=None, notes=None, kicker=None):
    s = '<section class="s-svg">'
    if kicker:
        s += '<p class="kicker">%s</p>' % kicker
    if title:
        s += "<h3>%s</h3>" % title
    s += '<div class="fig">%s</div>' % body
    if caption:
        s += '<p class="cap">%s</p>' % caption
    return s + _notes(notes) + "</section>"


def quote(text, who, notes=None):
    return (
        '<section class="s-quote"><blockquote>%s</blockquote>'
        '<p class="who">%s</p>%s</section>' % (text, who, _notes(notes))
    )


def lab(title, items, notes=None):
    s = '<section class="s-lab"><p class="kicker">Next lab</p>'
    s += "<h3>%s</h3><ol>" % title
    for it in items:
        s += "<li>%s</li>" % it
    s += "</ol>"
    return s + _notes(notes) + "</section>"


def takeaways(items, notes=None):
    s = '<section class="s-take"><p class="kicker">Take away</p><ul>'
    for it in items:
        s += "<li>%s</li>" % it
    s += "</ul>"
    return s + _notes(notes) + "</section>"


# --------------------------------------------------------------------------
# page template
# --------------------------------------------------------------------------

CSS = r"""
:root{
  --ink:#15181d; --ink-2:#414a58; --ink-3:#78828f;
  --bg:#fbfaf8; --panel:#ffffff; --rule:#e2ded6;
  --accent:#a4161a; --accent-2:#1d4e89; --ok:#1b6e46;
  --code-bg:#1c2027; --code-fg:#e8e6e3;
  --sans:"Helvetica Neue",Helvetica,Arial,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"SF Mono",ui-monospace,"JetBrains Mono",Menlo,Consolas,monospace;
}
html,body{background:var(--bg);}
.reveal{font-family:var(--sans); color:var(--ink); font-weight:400; font-size:40px;}
.reveal .slides{text-align:left;}
.reveal .slides section{padding:0 2.2rem; line-height:1.35; box-sizing:border-box;}
.reveal h1,.reveal h2,.reveal h3,.reveal h4{
  font-family:var(--sans); color:var(--ink); font-weight:700;
  letter-spacing:-.02em; text-transform:none; margin:0 0 .5em;
}
.reveal h1{font-size:2.5em; line-height:1.05;}
.reveal h2{font-size:1.9em; line-height:1.12;}
.reveal h3{font-size:1.2em; line-height:1.2;}
.reveal h4{font-size:.66em; color:var(--ink-2); font-weight:700;
  text-transform:uppercase; letter-spacing:.09em; margin-bottom:.7em;}
.reveal p{margin:0 0 .6em;}
.reveal a{color:var(--accent-2); text-decoration:none; border-bottom:1px solid #c9d6e6;}
.reveal em{font-style:italic; color:var(--ink);}
.reveal strong{font-weight:700;}

.kicker{font-size:.46em!important; text-transform:uppercase; letter-spacing:.14em;
  color:var(--accent); font-weight:700; margin:0 0 1.1em!important;}
.sub{font-size:.58em!important; color:var(--ink-2); max-width:22em; margin-top:.9em!important;}
.cap{font-size:.46em!important; color:var(--ink-3); margin-top:.9em!important;}

/* one-idea slides -- scoped so the fallback engine can still hide them */
.reveal .slides > section.s-big,
.reveal .slides > section.s-q,
.reveal .slides > section.s-part,
.reveal .slides > section.s-quote,
.reveal .slides > section.s-title{
  display:flex; flex-direction:column; justify-content:center;}
.s-big h2{font-size:2.3em; max-width:15em;}
.s-q h2{font-size:2.1em; max-width:15em; color:var(--accent-2);}
.s-q h2::after{content:""; display:block; width:2.4em; height:3px;
  background:var(--accent); margin-top:.5em;}
.s-part h2{font-size:2.4em;}

/* lists */
.reveal .s-list ul,.reveal .s-take ul,.reveal .s-lab ol{
  display:block; margin:0; font-size:.72em;}
.reveal .s-list li,.reveal .s-take li,.reveal .s-lab li{margin:0 0 .62em; line-height:1.4;}
.reveal .s-list.tight li{margin-bottom:.34em;}
.reveal .s-list li ul{font-size:.86em; margin-top:.35em; color:var(--ink-2);}
.reveal .s-lab{border-left:5px solid var(--accent-2); }
.reveal .s-take{border-left:5px solid var(--ok);}
.reveal .s-take li::marker{color:var(--ok);}

/* code */
.reveal pre{width:100%; box-shadow:none; margin:.3em 0; font-size:.48em;}
.reveal pre code{
  background:var(--code-bg); color:var(--code-fg); font-family:var(--mono);
  padding:1em 1.1em; border-radius:8px; max-height:none; line-height:1.5;
  overflow:auto; display:block; tab-size:2; font-weight:400;}
.reveal code:not(pre code){
  font-family:var(--mono); font-size:.86em; background:#efece6;
  padding:.08em .3em; border-radius:4px; color:var(--ink);}

/* two columns */
.cols{display:flex; gap:1.6rem; align-items:flex-start;}
.col{flex:1 1 0; min-width:0;}
.reveal .col ul{font-size:.66em; display:block;}
.reveal .col li{margin-bottom:.5em;}
.reveal .col pre{font-size:.42em;}
.reveal .col p{font-size:.66em; color:var(--ink-2);}

/* tables */
.tw{overflow-x:auto;}
.reveal table{font-size:.58em; border-collapse:collapse; width:100%;}
.reveal table th{
  text-align:left; border-bottom:2px solid var(--ink); padding:.45em .6em;
  font-weight:700; font-size:.9em; text-transform:uppercase; letter-spacing:.06em;}
.reveal table td{border-bottom:1px solid var(--rule); padding:.45em .6em;
  vertical-align:top;}
.reveal table tr:last-child td{border-bottom:none;}

.reveal .s-table.dense table{font-size:.46em;}
.reveal .s-table.dense table td,.reveal .s-table.dense table th{padding:.3em .55em;}

/* figures */
.fig{display:flex; justify-content:center; align-items:center; margin:.2em 0;}
.fig svg{max-width:100%; height:auto; max-height:62vh;}

/* quote */
.reveal blockquote{
  background:none; box-shadow:none; width:100%; font-size:1.05em; font-style:normal;
  border-left:5px solid var(--accent); padding:.1em 0 .1em .9em; margin:0; line-height:1.3;}
.who{font-size:.54em!important; color:var(--ink-3); margin-top:1em!important;
  text-transform:uppercase; letter-spacing:.1em;}

/* title slide */
.s-title .wk{font-size:.44em!important; text-transform:uppercase; letter-spacing:.16em;
  color:var(--accent); font-weight:700; margin:0 0 .8em!important;}
.s-title h1{margin-bottom:.25em;}
.s-title .tag{font-size:.55em!important; color:var(--ink-2); max-width:24em;}
.s-title .meta{font-size:.42em!important; color:var(--ink-3); margin-top:2em!important;
  border-top:1px solid var(--rule); padding-top:.9em;}

/* chrome */
.deck-chrome{position:fixed; bottom:14px; left:20px; right:20px; z-index:30;
  display:flex; justify-content:space-between; font:600 11px/1 var(--sans);
  color:var(--ink-3); letter-spacing:.08em; text-transform:uppercase;
  pointer-events:none;}
.reveal .progress{color:var(--accent); height:3px;}
.reveal .controls{color:var(--ink-3);}

/* ---------- fallback engine (no reveal.js) ---------- */
html.no-reveal body{margin:0;}
html.no-reveal .reveal .slides{position:static;}
html.no-reveal .reveal .slides > section{
  display:none; position:relative; width:100%;
  min-height:100vh; box-sizing:border-box;
  padding:6vh 7vw 12vh; font-size:calc(13px + 1.9vw);}
html.no-reveal .reveal .slides > section.fb-on{display:block;}
html.no-reveal .reveal .slides > section.fb-on.s-big,
html.no-reveal .reveal .slides > section.fb-on.s-q,
html.no-reveal .reveal .slides > section.fb-on.s-part,
html.no-reveal .reveal .slides > section.fb-on.s-quote,
html.no-reveal .reveal .slides > section.fb-on.s-title{
  display:flex; flex-direction:column; justify-content:center;}
html.no-reveal .notes{display:none;}
html.no-reveal.fb-notes .notes{
  display:block; margin-top:2em; padding:.9em 1.1em; background:#f2efe9;
  border-left:4px solid var(--ink-3); font-size:.5em; color:var(--ink-2);
  border-radius:0 6px 6px 0;}
html.no-reveal.fb-all .reveal .slides > section{
  display:block; min-height:0; border-bottom:1px solid var(--rule);
  page-break-after:always; break-after:page;}
.fb-bar{position:fixed; bottom:0; left:0; right:0; height:4px;
  background:var(--rule); z-index:40; display:none;}
html.no-reveal .fb-bar{display:block;}
.fb-bar i{display:block; height:100%; background:var(--accent); width:0;}
@media print{
  .deck-chrome,.fb-bar{display:none!important;}
  html.no-reveal .reveal .slides > section{display:block!important;}
}
"""

FALLBACK_JS = r"""
(function(){
  // Progressive enhancement: use reveal.js when it loads, otherwise a tiny
  // built-in presenter so the deck still works with no network in the room.
  function boot(){
    if (window.Reveal) {
      Reveal.initialize({
        hash:true, slideNumber:'c/t', controls:true, progress:true,
        transition:'none', backgroundTransition:'none',
        width:1280, height:800, margin:0.06,
        minScale:0.2, maxScale:1.6,
        plugins:[window.RevealHighlight, window.RevealNotes].filter(Boolean)
      });
      return;
    }
    var root=document.documentElement;
    root.classList.add('no-reveal');
    var slides=[].slice.call(document.querySelectorAll('.reveal .slides > section'));
    if(!slides.length) return;
    var bar=document.createElement('div');
    bar.className='fb-bar'; bar.innerHTML='<i></i>';
    document.body.appendChild(bar);
    var fill=bar.firstChild, i=0;
    function show(n){
      i=Math.max(0,Math.min(slides.length-1,n));
      slides.forEach(function(s,k){ s.classList.toggle('fb-on',k===i); });
      fill.style.width=((i+1)/slides.length*100)+'%';
      var c=document.getElementById('deck-pos');
      if(c) c.textContent=(i+1)+' / '+slides.length;
      try{ history.replaceState(null,'','#/'+i); }catch(e){}
      window.scrollTo(0,0);
    }
    var m=/^#\/(\d+)/.exec(location.hash||'');
    document.addEventListener('keydown',function(e){
      if(e.metaKey||e.ctrlKey||e.altKey) return;
      var k=e.key;
      if(k==='ArrowRight'||k==='ArrowDown'||k===' '||k==='PageDown'){show(i+1);e.preventDefault();}
      else if(k==='ArrowLeft'||k==='ArrowUp'||k==='PageUp'){show(i-1);e.preventDefault();}
      else if(k==='Home'){show(0);e.preventDefault();}
      else if(k==='End'){show(slides.length-1);e.preventDefault();}
      else if(k==='n'||k==='s'){root.classList.toggle('fb-notes');}
      else if(k==='a'){root.classList.toggle('fb-all');}
      else if(k==='f'){ if(document.fullscreenElement) document.exitFullscreen();
                        else document.documentElement.requestFullscreen(); }
    });
    document.addEventListener('click',function(e){
      if(e.target.closest('a')) return;
      show(i + (e.clientX > window.innerWidth*0.35 ? 1 : -1));
    });
    show(m?parseInt(m[1],10):0);
  }
  if(document.readyState==='loading')
    window.addEventListener('DOMContentLoaded',function(){setTimeout(boot,60);});
  else setTimeout(boot,60);
})();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="author" content="{author}">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{rev}/reveal.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/{hljs}/styles/atom-one-dark.min.css">
<style>{css}</style>
</head>
<body>
<div class="reveal"><div class="slides">
{slides}
</div></div>
<div class="deck-chrome"><span>{course}</span><span id="deck-pos">{wk}</span></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{rev}/reveal.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{rev}/plugin/highlight/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/{rev}/plugin/notes/notes.min.js"></script>
<script>{fallback}</script>
</body>
</html>
"""


def title_slide(wk, title, tagline):
    return (
        '<section class="s-title">'
        '<p class="wk">%s</p><h1>%s</h1><p class="tag">%s</p>'
        '<p class="meta">%s &middot; %s &middot; %s</p>'
        "</section>" % (wk, title, tagline, AUTHOR, COURSE, YEAR)
    )


def build_deck(num, title, tagline, slides, outname=None):
    wk = "Week %02d" % num
    body = title_slide(wk, title, tagline) + "\n".join(slides)
    page = PAGE.format(
        title="%s — %s" % (wk, plain(title)),
        author=AUTHOR,
        course=COURSE,
        wk=wk,
        rev=REVEAL,
        hljs=HLJS,
        css=CSS,
        slides=body,
        fallback=FALLBACK_JS,
    )
    os.makedirs(OUT, exist_ok=True)
    name = outname or ("w%02d-%s.html" % (num, slugify(title)))
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(page)
    n = body.count("<section")
    return name, n


def plain(s):
    """Strip tags and resolve entities -- for filenames and <title>."""
    return _html.unescape(re.sub("<[^>]+>", "", s))


def slugify(s):
    s = plain(s).lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:44]
