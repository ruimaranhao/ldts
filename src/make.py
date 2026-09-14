#!/usr/bin/env python3
"""Build all LDTS decks plus the index hub."""

import os
import re

import build as B
from content_a import W01, W02, W03, W04
from content_b import W05, W06, W07, W08, W09
from content_c import W10, W11, W12, W13

WEEKS = [
    (1, "Git &amp; GitHub", "Version control as a design tool, not a chore.", "Foundations", W01),
    (2, "Java &amp; the Build", "What C++ did not prepare you for, and why the build must run without you.", "Foundations", W02),
    (3, "Test Automation", "Error, fault, failure &mdash; and the first JUnit 5 test.", "Testing", W03),
    (4, "Testing Strategies &amp; Coverage", "Black box, white box, and what coverage does not tell you.", "Testing", W04),
    (5, "Test Doubles &amp; CI", "Testing in isolation, and making the suite run without you.", "Testing", W05),
    (6, "SOLID", "Five heuristics against rigidity, fragility, immobility and viscosity.", "Design", W06),
    (7, "UML for Design", "Drawing to decide. Class, sequence and state diagrams.", "Design", W07),
    (8, "Design Patterns I", "Creational and structural patterns, and where each one earns its place.", "Design", W08),
    (9, "Design Patterns II &amp; MVC", "Behavioural patterns, and where each class belongs.", "Design", W09),
    (10, "Code Smells &amp; Refactoring", "Reading your own code as a critic, then changing it safely.", "Quality", W10),
    (11, "Mutation &amp; Property-Based Testing", "Two honest answers to &lsquo;are my tests any good?&rsquo;", "Quality", W11),
    (12, "Demos &amp; Designing for Change", "Show what you built, then absorb a new requirement.", "Project", W12),
    (13, "Review &amp; AI-Assisted Development", "The skill that transfers, and where the degree goes next.", "Project", W13),
]

MARKS = {
    6: "Test #1 &middot; 15%",
    7: "Project released",
    11: "Test #2 &middot; 20% &nbsp;&middot;&nbsp; intermediate delivery",
    12: "Demos &nbsp;&middot;&nbsp; requirement drop &middot; 10% of project",
}

INDEX_CSS = """
:root{--ink:#15181d;--ink-2:#414a58;--ink-3:#78828f;--bg:#fbfaf8;--panel:#fff;
 --rule:#e2ded6;--accent:#a4161a;--accent-2:#1d4e89;
 --sans:"Helvetica Neue",Helvetica,Arial,system-ui,-apple-system,"Segoe UI",sans-serif;}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
 line-height:1.5;-webkit-font-smoothing:antialiased}
.wrap{max-width:940px;margin:0 auto;padding-block:64px 96px;padding-left:24px;padding-right:24px}
header{border-bottom:2px solid var(--ink);padding-bottom:26px;margin-bottom:14px}
.kick{font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);
 font-weight:700;margin:0 0 12px}
h1{font-size:clamp(30px,5.4vw,46px);letter-spacing:-.025em;margin:0 0 10px;line-height:1.06}
.lede{font-size:17px;color:var(--ink-2);max-width:44em;margin:0}
.meta{font-size:13px;color:var(--ink-3);margin-top:20px}
.block-h{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3);
 font-weight:700;margin:38px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--rule)}
a.card{display:flex;gap:18px;align-items:baseline;text-decoration:none;color:inherit;
 padding:16px 18px;margin:0 -18px;border-radius:10px;transition:background .12s}
a.card:hover{background:#f2efe9}
.num{font-size:13px;font-weight:700;color:var(--accent);min-width:34px;letter-spacing:.05em;
 font-variant-numeric:tabular-nums;padding-top:3px}
.body{flex:1;min-width:0}
.t{font-size:19px;font-weight:700;letter-spacing:-.015em;margin:0 0 3px}
.d{font-size:14.5px;color:var(--ink-2);margin:0}
.tag{display:inline-block;margin-top:8px;font-size:11px;font-weight:700;letter-spacing:.09em;
 text-transform:uppercase;color:var(--accent-2);border:1px solid #c9d6e6;background:#f2f6fb;
 padding:3px 8px;border-radius:20px}
.n{font-size:12px;color:var(--ink-3);white-space:nowrap;font-variant-numeric:tabular-nums;
 padding-top:6px}
footer{margin-top:56px;padding-top:22px;border-top:1px solid var(--rule);
 font-size:13.5px;color:var(--ink-3)}
footer code{font-family:ui-monospace,Menlo,Consolas,monospace;background:#efece6;
 padding:.1em .35em;border-radius:4px;color:var(--ink-2)}
footer p{margin:0 0 8px}
@media (max-width:560px){a.card{gap:12px;padding:14px 12px;margin:0 -12px}.num{min-width:26px}}
"""


def main():
    built = []
    for num, title, tagline, block, slides in WEEKS:
        name, n = B.build_deck(num, title, tagline, slides)
        built.append((num, title, tagline, block, name, n))
        print("w%02d  %-44s %3d slides  %s" % (num, re.sub("<[^>]+>", "", title), n, name))

    rows, last_block = [], None
    for num, title, tagline, block, name, n in built:
        if block != last_block:
            rows.append('<p class="block-h">%s</p>' % block)
            last_block = block
        mark = '<span class="tag">%s</span>' % MARKS[num] if num in MARKS else ""
        rows.append(
            '<a class="card" href="%s"><span class="num">%02d</span>'
            '<span class="body"><p class="t">%s</p><p class="d">%s</p>%s</span>'
            '<span class="n">%d slides</span></a>' % (name, num, title, tagline, mark, n)
        )

    total = sum(b[5] for b in built)
    index = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>LDTS Lecture Slides</title><style>%s</style></head><body>
<div class="wrap">
<header>
<p class="kick">L.EIC014 &middot; FEUP &middot; %s</p>
<h1>Software Design and Testing Laboratory</h1>
<p class="lede">Thirteen weeks of lecture slides. Design, test, refactor &mdash;
in that order, repeatedly.</p>
<p class="meta">%s &middot; %d slides across 13 decks</p>
</header>
%s
<footer>
<p><strong>Presenting.</strong> Open a deck and use the arrow keys. <code>F</code> full screen,
<code>S</code> speaker notes, <code>ESC</code> overview, <code>?</code> for all shortcuts.</p>
<p><strong>Exporting to PDF.</strong> Append <code>?print-pdf</code> to the deck URL and print to PDF
from Chrome, background graphics on.</p>
<p><strong>Offline.</strong> The decks load reveal.js from a CDN and fall back to a built-in
presenter if there is no network, so they work in a lecture room either way.</p>
<p><strong>Editing.</strong> Slides are generated from <code>content_a/b/c.py</code>; run
<code>python3 make.py</code> to rebuild.</p>
</footer>
</div></body></html>""" % (INDEX_CSS, B.YEAR, B.AUTHOR, total, "\n".join(rows))

    with open(os.path.join(B.OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index)
    print("\nindex.html  ·  %d slides total" % total)


if __name__ == "__main__":
    main()
