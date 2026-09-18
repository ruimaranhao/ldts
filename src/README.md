# LDTS — Lecture Slides

Software Design and Testing Laboratory (L.EIC014), FEUP.
Rui Maranhão · 2026/2027 · 13 decks, 425 slides.

Open `index.html` for the week index, or open any `wNN-*.html` directly.

---

## Presenting

| Key | Does |
|---|---|
| `→` `←` `Space` | next / previous slide |
| `F` | full screen |
| `S` | speaker notes (opens a second window under reveal.js) |
| `Esc` | slide overview |
| `?` | all reveal.js shortcuts |

Click on the right two-thirds of the slide to advance, left third to go back.

### Exporting to PDF

Append `?print-pdf` to the deck URL, then print to PDF from Chrome with
**Background graphics** on and margins set to **None**. This is how you produce
the Moodle handout version.

Under the offline fallback (see below), press `A` to lay every slide out in one
scrolling page, then print.

### Offline

Each deck loads reveal.js from cdnjs. If there is no network in the lecture
room, a small presenter engine built into the file takes over automatically —
same keys, same slides, no styling loss. Extra keys in that mode: `N` toggles
speaker notes inline, `A` shows all slides in one page.

To remove the CDN dependency entirely, download reveal.js 5.1.0, drop it beside
the decks, and replace the four `https://cdnjs.cloudflare.com/...` URLs in each
file with local paths.

### Publishing to GitHub Pages

The repo ships a workflow at `.github/workflows/pages.yml` that regenerates the
decks from `src/` on every push to `main` and deploys them. Enable it once:

1. Push this folder to a repo.
2. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
3. Push to `main`. The decks appear at
   `https://<user>.github.io/<repo>/`.

The Python source is then the only thing you edit — the published HTML is a
build artefact, never committed.

If you would rather not use Actions, commit the generated `.html` files at the
repo root, set **Pages → Source: Deploy from a branch → main / (root)**, and
rebuild locally before each push. Keep `.nojekyll` either way.

### Type size

The decks set their own base size (40px on reveal's 1280×800 canvas) because
they do not load a reveal theme. If you want everything larger or smaller,
change one line in `src/build.py`:

```css
.reveal{ ... font-size:40px;}
```

and rebuild. Every other size in the deck is relative to it.

---

## The 13 weeks

| # | Deck | Block | Assessment |
|---|---|---|---|
| 1 | Git & GitHub | Foundations | |
| 2 | Java & the Build | Foundations | |
| 3 | Test Automation | Testing | |
| 4 | Testing Strategies & Coverage | Testing | |
| 5 | Test Doubles & CI | Testing | |
| 6 | SOLID | Design | **Test #1 · 20%** |
| 7 | UML for Design | Design | **Project released** |
| 8 | Design Patterns I | Design | |
| 9 | Design Patterns II & MVC | Design | |
| 10 | Code Smells & Refactoring | Quality | |
| 11 | Mutation & Property-Based Testing | Quality | **Test #2 · 20%** · intermediate delivery |
| 12 | Demos & Designing for Change | Project | **Demos** · **requirement drop · 10%** |
| 13 | Review & AI-Assisted Development | Project | |

### What changed from 2025/26

- Git and Java compressed from four weeks to two; the two recovered weeks go to
  mutation testing, property-based testing, CI and code review.
- Design content moved earlier so the project (released week 7) can use it.
- Spock removed from the required path; property-based testing is jqwik, which
  is a JUnit 5 engine and needs no second language.
- New decks for material that previously ran on external links only: SOLID, UML,
  code smells and refactoring, MVC, mutation testing, PBT, CI, code review.
- Explicit AI-assistance policy (week 1) and a week on verification and review
  of generated code (week 13).
- Assessment rebalanced: Test #1 (multiple choice, week 6) gates the
  foundations; Test #2 (week 11) is done in the IDE; the project adds an
  individual defence.

---

## Editing

Slides are generated, not hand-written HTML:

```
src/build.py        theme, page template, slide helpers, fallback engine
src/content_a.py    weeks 1-4
src/content_b.py    weeks 5-9
src/content_c.py    weeks 10-13
src/make.py         week table, index hub -> writes decks/
```

```bash
cd src && python3 make.py      # rebuilds every deck and index.html
```

Slide helpers: `big`, `q`, `part`, `bullets`, `code`, `two`, `table`, `svg`,
`quote`, `lab`, `takeaways`. All take an optional `notes=` for speaker notes.
Content strings are HTML, so `<em>`, `<strong>` and `<code>` work inline.

Adding a slide is one call in the relevant week's list. Adding a week is one
entry in `WEEKS` in `make.py`.

## Notes

- Every code snippet targets Java 21, JUnit 5, Mockito 5, jqwik 1.8, PIT 1.15
  and Gradle Kotlin DSL.
- The running example throughout is the Lanterna project (Arena, Hero, Element,
  GUI adapter), so the lectures and the project use one vocabulary.
- Figures are inline SVG — no image files, nothing to lose.
- Not carried over: `head-first-design-patterns-compressed.pdf` from the 2025/26
  Moodle. Hosting the full book is a copyright exposure; the book is in the
  reading list instead.
