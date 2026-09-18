#!/usr/bin/env python3
"""Weeks 5-9: Doubles & CI · SOLID · UML · Patterns I · Patterns II + MVC."""

from build import (big, bullets, code, lab, part, q, quote, svg, table,
                   takeaways, two)

# ---------------------------------------------------------------- SVG figures

PYRAMID = """
<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="15">
  <polygon points="350,20 440,110 260,110" fill="#a4161a" opacity=".85"/>
  <polygon points="260,110 440,110 520,205 180,205" fill="#1d4e89" opacity=".8"/>
  <polygon points="180,205 520,205 610,305 90,305" fill="#1b6e46" opacity=".8"/>
  <g fill="#fff" text-anchor="middle" font-weight="700">
    <text x="350" y="95">end-to-end</text>
    <text x="350" y="170">integration</text>
    <text x="350" y="268">unit</text>
  </g>
  <g fill="#78828f" font-size="13" text-anchor="start">
    <text x="628" y="80">few, slow, brittle</text>
    <text x="628" y="165">some</text>
    <text x="628" y="268">many, fast, precise</text>
  </g>
</svg>
"""

DOUBLE = """
<svg viewBox="0 0 760 220" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="15">
  <defs><marker id="d1" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
    <path d="M0 0 L9 4.5 L0 9 z" fill="#414a58"/></marker></defs>
  <g fill="none" stroke="#15181d" stroke-width="2.5">
    <rect x="60" y="60" width="150" height="70" rx="8"/>
    <rect x="330" y="60" width="150" height="70" rx="8"/>
  </g>
  <rect x="330" y="60" width="150" height="70" rx="8" fill="none"
        stroke="#a4161a" stroke-width="2.5" stroke-dasharray="7 5"/>
  <rect x="590" y="60" width="150" height="70" rx="8" fill="none"
        stroke="#c9c4ba" stroke-width="2.5" stroke-dasharray="3 6"/>
  <g text-anchor="middle" font-weight="700" fill="#15181d">
    <text x="135" y="102">Order</text>
    <text x="405" y="95" fill="#a4161a">MailService</text>
    <text x="405" y="115" fill="#a4161a" font-size="13" font-weight="400">(double)</text>
    <text x="665" y="95" fill="#78828f">real SMTP</text>
    <text x="665" y="115" fill="#78828f" font-size="13" font-weight="400">not in the test</text>
  </g>
  <path d="M215 95 L325 95" stroke="#414a58" stroke-width="2.5" fill="none" marker-end="url(#d1)"/>
  <path d="M485 95 L585 95" stroke="#c9c4ba" stroke-width="2" fill="none" stroke-dasharray="4 5"/>
  <text x="135" y="42" text-anchor="middle" fill="#78828f" font-size="13">unit under test</text>
  <text x="380" y="180" text-anchor="middle" fill="#78828f" font-size="14">
    You are not testing the mail server. You are testing that Order asks for mail.</text>
</svg>
"""

UMLCLASS = """
<svg viewBox="0 0 760 380" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="13">
  <g stroke="#15181d" stroke-width="2" fill="#fff">
    <rect x="290" y="16" width="190" height="76"/>
    <rect x="60"  y="185" width="180" height="76"/>
    <rect x="290" y="185" width="180" height="76"/>
    <rect x="530" y="185" width="180" height="76"/>
    <rect x="290" y="300" width="190" height="62"/>
  </g>
  <g stroke="#15181d" stroke-width="1.5">
    <line x1="290" y1="44" x2="480" y2="44"/><line x1="290" y1="68" x2="480" y2="68"/>
    <line x1="60"  y1="213" x2="240" y2="213"/>
    <line x1="290" y1="213" x2="470" y2="213"/>
    <line x1="530" y1="213" x2="710" y2="213"/>
    <line x1="290" y1="328" x2="480" y2="328"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="#15181d">
    <text x="385" y="36" font-style="italic">Element</text>
    <text x="150" y="205">Hero</text><text x="380" y="205">Wall</text><text x="620" y="205">Monster</text>
    <text x="385" y="320">Position</text>
  </g>
  <g fill="#414a58" font-family="SF Mono,Menlo,monospace" font-size="12">
    <text x="300" y="60"># position: Position</text>
    <text x="300" y="84">+ draw(gui): void</text>
    <text x="70"  y="231">+ move(d): Hero</text>
    <text x="300" y="231">+ draw(gui): void</text>
    <text x="540" y="231">+ chase(h): Monster</text>
    <text x="300" y="346">+ x: int  + y: int</text>
  </g>
  <g stroke="#15181d" stroke-width="2" fill="none">
    <path d="M150 185 L150 140 L385 140 L385 96"/>
    <path d="M380 185 L380 140"/>
    <path d="M620 185 L620 140 L385 140"/>
  </g>
  <path d="M385 92 L376 108 L394 108 z" fill="#fff" stroke="#15181d" stroke-width="2"/>
  <path d="M385 261 L385 300" stroke="#15181d" stroke-width="2"/>
  <path d="M385 261 L376 275 L385 289 L394 275 z" fill="#15181d"/>
  <text x="400" y="285" fill="#78828f">1</text>
  <text x="596" y="128" fill="#78828f">generalisation</text>
  <text x="404" y="278" fill="#78828f" font-size="12"> </text>
</svg>
"""

SEQ = """
<svg viewBox="0 0 760 360" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="13">
  <defs><marker id="s1" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
    <path d="M0 0 L10 5 L0 10 z" fill="#15181d"/></marker>
    <marker id="s2" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
    <path d="M0 2 L10 5 L0 8" fill="none" stroke="#78828f" stroke-width="1.6"/></marker></defs>
  <g stroke="#15181d" stroke-width="2" fill="#fff">
    <rect x="50" y="16" width="130" height="38"/>
    <rect x="300" y="16" width="130" height="38"/>
    <rect x="560" y="16" width="140" height="38"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="#15181d">
    <text x="115" y="41">:Game</text><text x="365" y="41">:Arena</text><text x="630" y="41">:Hero</text>
  </g>
  <g stroke="#c9c4ba" stroke-width="1.5" stroke-dasharray="6 6">
    <line x1="115" y1="54" x2="115" y2="330"/>
    <line x1="365" y1="54" x2="365" y2="330"/>
    <line x1="630" y1="54" x2="630" y2="330"/>
  </g>
  <g fill="#e8e4dc" stroke="#15181d" stroke-width="1.5">
    <rect x="107" y="86" width="16" height="200"/>
    <rect x="357" y="110" width="16" height="150"/>
    <rect x="622" y="140" width="16" height="70"/>
  </g>
  <g stroke="#15181d" stroke-width="2" marker-end="url(#s1)">
    <line x1="123" y1="110" x2="355" y2="110"/>
    <line x1="373" y1="140" x2="620" y2="140"/>
  </g>
  <g stroke="#78828f" stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#s2)">
    <line x1="620" y1="210" x2="375" y2="210"/>
    <line x1="355" y1="260" x2="125" y2="260"/>
  </g>
  <g fill="#15181d" font-family="SF Mono,Menlo,monospace" font-size="12">
    <text x="150" y="103">processKey(UP)</text>
    <text x="400" y="133">moveHero(UP)</text>
  </g>
  <g fill="#78828f" font-family="SF Mono,Menlo,monospace" font-size="12">
    <text x="420" y="203">newPosition</text>
    <text x="170" y="253">redraw</text>
  </g>
</svg>
"""

STATE = """
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="14">
  <defs><marker id="t1" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto">
    <path d="M0 0 L10 5 L0 10 z" fill="#15181d"/></marker></defs>
  <circle cx="52" cy="90" r="11" fill="#15181d"/>
  <g fill="#fff" stroke="#15181d" stroke-width="2.5">
    <rect x="120" y="60" width="150" height="60" rx="26"/>
    <rect x="360" y="60" width="150" height="60" rx="26"/>
    <rect x="360" y="190" width="150" height="60" rx="26"/>
    <rect x="600" y="60" width="120" height="60" rx="26"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="#15181d">
    <text x="195" y="97">Menu</text><text x="435" y="97">Running</text>
    <text x="435" y="227">Paused</text><text x="660" y="97">GameOver</text>
  </g>
  <g stroke="#15181d" stroke-width="2" fill="none" marker-end="url(#t1)">
    <path d="M63 90 L116 90"/>
    <path d="M270 90 L356 90"/>
    <path d="M448 120 L448 186"/>
    <path d="M422 186 L422 124"/>
    <path d="M510 90 L596 90"/>
    <path d="M660 120 C660 190 560 260 300 250 L280 150 L240 122"/>
  </g>
  <g fill="#a4161a" font-size="12.5" font-family="SF Mono,Menlo,monospace">
    <text x="286" y="80">start</text>
    <text x="458" y="160">ESC</text>
    <text x="336" y="160">ESC</text>
    <text x="524" y="80">heroDied</text>
    <text x="430" y="286">restart</text>
  </g>
</svg>
"""

MVC = """
<svg viewBox="0 0 760 320" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="15">
  <defs><marker id="m1" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
    <path d="M0 0 L9 4.5 L0 9 z" fill="#414a58"/></marker></defs>
  <g fill="none" stroke="#15181d" stroke-width="2.5">
    <rect x="300" y="20" width="170" height="66" rx="8"/>
    <rect x="60"  y="200" width="170" height="66" rx="8"/>
    <rect x="530" y="200" width="170" height="66" rx="8"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="#15181d">
    <text x="385" y="52">Controller</text><text x="385" y="72" font-size="12" font-weight="400" fill="#78828f">reads input, decides</text>
    <text x="145" y="232">Model</text><text x="145" y="252" font-size="12" font-weight="400" fill="#78828f">state and rules</text>
    <text x="615" y="232">Viewer</text><text x="615" y="252" font-size="12" font-weight="400" fill="#78828f">draws, nothing else</text>
  </g>
  <g stroke="#414a58" stroke-width="2.5" fill="none" marker-end="url(#m1)">
    <path d="M320 88 L180 196"/>
    <path d="M452 88 L586 196"/>
    <path d="M230 218 L525 218"/>
  </g>
  <g fill="#78828f" font-size="13">
    <text x="188" y="138">mutates</text>
    <text x="500" y="138">tells to draw</text>
    <text x="332" y="208">reads</text>
  </g>
  <text x="380" y="300" text-anchor="middle" fill="#a4161a" font-size="14" font-weight="700">
    The Model must not import Lanterna. Ever.</text>
</svg>
"""

# ================================================================== WEEK 05

W05 = [
    part("Part one", "Test-first"),
    q("When can you start testing?"),
    big("Before the code exists.",
        "The specification is enough."),
    bullets("Why write the test first", [
        "It forces you to decide what the method <em>promises</em>",
        "It forces you to design the interface before the implementation",
        "You find out immediately whether the code is testable",
        "You are never afraid to change code that has a suite behind it",
    ]),
    big("A test case is an incomplete specification.",
        "One concrete point on a contract you could otherwise only describe in prose."),
    code("Design by contract, made executable", "java", r"""
// contract for Dictionary.put(key, value)
//   pre  : key != null
//   post : count == old count + 1  (if key was absent)
//          get(key) == value

@Test
void putIncreasesCountWhenKeyIsNew() {
    Dictionary d = new Dictionary();
    d.put("a", 1);

    d.put("b", 2);

    assertEquals(2, d.count());
    assertEquals(2, d.get("b"));
}
"""),
    bullets("Red &rarr; Green &rarr; Refactor", [
        "<strong>Red</strong> &mdash; write a failing test. Watch it fail, or you do not know it works.",
        "<strong>Green</strong> &mdash; the simplest code that passes",
        "<strong>Refactor</strong> &mdash; clean up, suite still green",
        "The third step is the one everyone skips and the one that pays",
    ]),
    part("Part two", "Types of tests"),
    q("What is the best strategy to test a whole system?"),
    big("Divide and conquer."),
    svg("The pyramid", PYRAMID,
        caption="Push tests down. A bug caught by a unit test costs minutes; the same bug caught end-to-end costs an afternoon."),
    q("From an object-oriented point of view, what is the smallest testable part?"),
    big("A class and its methods.",
        "An object is a cohesive set of data and behaviour &mdash; that is exactly a unit."),
    q("Which methods deserve a test?"),
    table("A pragmatic filter", ["Method", "Test it?", "Why"], [
        ["Constructor with invariants", "Yes", "It is where invalid state gets in"],
        ["Business logic", "Yes", "This is the actual product"],
        ["Trivial getter", "No", "Nothing to break"],
        ["Generated <code>equals</code>", "No", "You did not write it"],
        ["Private helper", "Indirectly", "Through the public method that uses it"],
    ]),
    big("If a private method is complex enough to need its own test,",
        "it probably wants to be its own class."),
    part("Part three", "Testing in isolation"),
    q("Can you test a class that depends on three other classes?"),
    two("Two strategies", "Test A and B together", """
<ul><li>Tests A, B <em>and</em> their interplay</li>
<li>Fewer moving parts to write</li>
<li>When it fails, which one is broken?</li>
<li>B might be slow, or a network</li></ul>""",
        "Test A in isolation", """
<ul><li>Replace B with a double</li>
<li>Failure points at A</li>
<li>Fast and deterministic</li>
<li>You must know B's contract</li></ul>"""),
    svg("A test double", DOUBLE),
    bullets("Why doubles exist", [
        "Isolate the unit under test",
        "Remove slow or unreliable dependencies (network, clock, filesystem, terminal)",
        "Reach states that are hard to produce for real",
        "Break the dependency between two teams working in parallel",
    ]),
    q("Stub or mock? They are not synonyms."),
    two("The distinction", "Stub", """
<p>Provides canned answers.</p>
<ul><li>You assert on the <strong>result</strong></li>
<li><em>state verification</em></li>
<li>&ldquo;Given the mail service says OK, the order is complete&rdquo;</li></ul>""",
        "Mock", """
<p>Pre-programmed with expectations.</p>
<ul><li>You assert on the <strong>interaction</strong></li>
<li><em>behaviour verification</em></li>
<li>&ldquo;The order <em>asked</em> the mail service to send&rdquo;</li></ul>"""),
    code("A stub, by hand", "java", r"""
class MailServiceStub implements MailService {
    private final List<Message> sent = new ArrayList<>();

    @Override public void send(Message msg) { sent.add(msg); }
    public int messagesSent() { return sent.size(); }
}

@Test
void unfilledOrderSendsMail() {
    MailServiceStub mailer = new MailServiceStub();
    Order order = new Order(mailer);

    order.fill(emptyWarehouse);

    assertEquals(1, mailer.messagesSent());   // state verification
}
"""),
    code("A mock, with Mockito", "java", r"""
@Test
void unfilledOrderAsksMailerToSend() {
    MailService mailer = mock(MailService.class);
    Order order = new Order(mailer);

    order.fill(emptyWarehouse);

    verify(mailer).send(any(Message.class));  // behaviour verification
    verifyNoMoreInteractions(mailer);
}
"""),
    code("Stubbing return values with Mockito", "java", r"""
Warehouse warehouse = mock(Warehouse.class);
when(warehouse.hasInventory("sword", 1)).thenReturn(true);
when(warehouse.hasInventory("shield", 1)).thenReturn(false);

Order order = new Order("shield", 1);
order.fill(warehouse);

assertFalse(order.isFilled());
""", caption="<code>when</code> stubs. <code>verify</code> mocks. Most tests want <code>when</code>."),
    big("Do not mock what you do not own.",
        "Mock <em>your</em> interfaces. Wrap third-party APIs first, then mock the wrapper."),
    q("How do you test a game that draws to a terminal?"),
    bullets("You do not draw", [
        "Put an interface between your code and Lanterna: <code>GUI</code>",
        "Production: <code>LanternaGUI implements GUI</code>",
        "Tests: <code>mock(GUI.class)</code>, then <code>verify(gui).drawHero(...)</code>",
        "This single abstraction is worth more marks than any feature you will add",
    ]),
    part("Part four", "Continuous integration"),
    q("Your tests pass. On your laptop. On Tuesday."),
    big("A test suite nobody runs is a comment.",
        "CI is what makes running it involuntary."),
    code("A pipeline that fits on one slide", "yaml", r"""
name: build
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: { distribution: temurin, java-version: '21' }
      - run: ./gradlew build jacocoTestReport
      - uses: actions/upload-artifact@v4
        with: { name: coverage, path: build/reports/jacoco }
""", caption="Every push. Every pull request. No opinions involved."),
    bullets("What the pipeline should refuse to merge", [
        "A failing test",
        "A drop in branch coverage below the agreed floor",
        "New Checkstyle or SpotBugs violations",
        "From week 11: a mutation score below the floor",
    ]),
    lab("Lab 5", [
        "Introduce the <code>GUI</code> interface and mock it",
        "Convert three hand-written stubs to Mockito",
        "Write one test that fails for the right reason, then make it pass",
        "Turn on GitHub Actions for your project repository",
    ]),
    takeaways([
        "Write the test first &mdash; it is a design activity, not a checking activity",
        "Stubs verify state; mocks verify interaction",
        "Isolate the terminal behind an interface you own",
        "Green on CI, or it did not happen",
    ]),
]

# ================================================================== WEEK 06

W06 = [
    part("Design", "Five principles"),
    q("Your code works. Why would anyone want to change how it is arranged?"),
    big("Because the next requirement is already on its way."),
    quote("A design is rigid when a single change forces a cascade of changes in dependent modules.",
          "Robert C. Martin"),
    bullets("Four symptoms of rot", [
        "<strong>Rigidity</strong> &mdash; a small change forces many others",
        "<strong>Fragility</strong> &mdash; a change breaks something unrelated",
        "<strong>Immobility</strong> &mdash; you cannot reuse a part without dragging the whole",
        "<strong>Viscosity</strong> &mdash; the wrong thing is easier to do than the right one",
    ]),
    big("S O L I D",
        "Five heuristics that push back on all four."),
    part("S", "Single Responsibility"),
    big("A class should have one reason to change."),
    code("Two reasons to change", "java", r"""
class Hero {
    private Position position;

    public void move(Direction d) { ... }          // game rules

    public void draw(TextGraphics g) {             // presentation
        g.setForegroundColor(TextColor.ANSI.RED);
        g.putString(position.x(), position.y(), "H");
    }

    public void saveToFile(Path path) { ... }      // persistence
}
""", caption="Change the colour scheme &rarr; recompile the game rules. Three responsibilities, one class."),
    code("Split by reason to change", "java", r"""
record Hero(Position position) {
    Hero move(Direction d) { return new Hero(position.translate(d)); }
}

class HeroViewer implements ElementViewer<Hero> {
    public void draw(Hero hero, GUI gui) { gui.drawHero(hero.position()); }
}

class HeroRepository { void save(Hero hero, Path path) { ... } }
"""),
    q("&ldquo;One responsibility&rdquo; sounds subjective. Is it?"),
    big("Ask who asks for the change.",
        "Game designer, artist, ops engineer &mdash; three people, three classes."),
    part("O", "Open/Closed"),
    big("Open for extension. Closed for modification.",
        "New behaviour should mean new code, not edited code."),
    code("Closed for extension", "java", r"""
class Monster {
    void act(Arena arena) {
        if (type == Type.CHASER)      chase(arena);
        else if (type == Type.RANDOM) wander(arena);
        else if (type == Type.SLEEPER) { }
        // a fourth monster means editing this method again
    }
}
"""),
    code("Open for extension", "java", r"""
interface Monster { Position nextPosition(Arena arena); }

class Chaser  implements Monster { ... }
class Wanderer implements Monster { ... }
class Sleeper implements Monster { ... }

// a fourth monster is a new file; nothing existing is touched
""", caption="This is the Strategy pattern, arrived at from a principle rather than a catalogue."),
    part("L", "Liskov Substitution"),
    big("A subtype must be usable wherever its supertype is,",
        "without the caller knowing."),
    code("The classic violation", "java", r"""
class Rectangle {
    void setWidth(int w)  { this.width = w; }
    void setHeight(int h) { this.height = h; }
    int area() { return width * height; }
}

class Square extends Rectangle {
    void setWidth(int w)  { this.width = w; this.height = w; }
    void setHeight(int h) { this.width = h; this.height = h; }
}

// caller: r.setWidth(5); r.setHeight(4); assertEquals(20, r.area());
// passes for Rectangle, fails for Square
""", caption="A square <em>is a</em> rectangle in geometry. It is not a subtype in code."),
    bullets("What subclasses must not do", [
        "Strengthen preconditions &mdash; demand more than the parent",
        "Weaken postconditions &mdash; promise less than the parent",
        "Throw new exception types the caller cannot expect",
        "Silently do nothing where the parent did something",
    ]),
    big("If you find yourself writing <code>if (x instanceof Y)</code>,",
        "you have probably broken this one already."),
    part("I", "Interface Segregation"),
    big("No client should depend on methods it does not use."),
    code("A fat interface", "java", r"""
interface GameElement {
    void draw(GUI gui);
    void update(Arena arena);
    void onCollision(GameElement other);
    void playSound();
    void save(Path path);
}

// Wall implements five methods. Four of them are empty.
"""),
    code("Segregated", "java", r"""
interface Drawable  { void draw(GUI gui); }
interface Updatable { void update(Arena arena); }
interface Collidable { void onCollision(GameElement other); }

class Wall   implements Drawable, Collidable { ... }
class Hero   implements Drawable, Updatable, Collidable { ... }
""", caption="Empty method bodies are the smell. They mean the interface is too big."),
    part("D", "Dependency Inversion"),
    big("Depend on abstractions, not on concretions.",
        "High-level policy must not depend on low-level detail."),
    code("Inverted", "java", r"""
// before: the game owns a terminal
class Game {
    private final LanternaGUI gui = new LanternaGUI();   // concrete, untestable
}

// after: the game is handed something that can draw
class Game {
    private final GUI gui;
    Game(GUI gui) { this.gui = gui; }                    // injected
}

// production: new Game(new LanternaGUI());
// test:       new Game(mock(GUI.class));
"""),
    big("Dependency injection is not a framework.",
        "It is a constructor parameter."),
    q("Which principle does &ldquo;the Model must not import Lanterna&rdquo; enforce?"),
    table("The five, in one table", ["", "Principle", "The question it asks"], [
        ["S", "Single responsibility", "Who asks for this class to change?"],
        ["O", "Open/closed", "Can I add behaviour without editing?"],
        ["L", "Liskov substitution", "Can I swap the subtype in blindly?"],
        ["I", "Interface segregation", "Is any implementer writing empty methods?"],
        ["D", "Dependency inversion", "Does policy depend on detail?"],
    ]),
    big("SOLID is a set of heuristics, not laws.",
        "Applied without judgement, they produce a hundred one-method classes."),
    big("Test #1 is after this week.",
        "Weeks 1&ndash;6. Multiple choice, 60 minutes, individual. 20%."),
    lab("Lab 6", [
        "Take the supplied <code>Hero</code> implementation and find every SOLID violation",
        "Fix them one principle at a time, keeping the suite green",
        "Justify each change in one sentence &mdash; this is what the report asks for",
    ]),
    takeaways([
        "One reason to change, per class",
        "New behaviour = new class, not an edited <code>if</code>",
        "<code>instanceof</code> in a caller is usually a broken abstraction",
        "Inject dependencies &mdash; it is what makes the code testable at all",
    ]),
]

# ================================================================== WEEK 07

W07 = [
    part("Design", "Drawing before building"),
    q("Why draw a diagram when the code is the truth?"),
    bullets("Because a diagram is cheaper", [
        "You can throw away a bad design in ten minutes, not ten days",
        "It is the fastest way to argue with two teammates",
        "It shows structure the code hides across forty files",
        "In the project report, it is how you <em>justify</em> your design",
    ]),
    big("Draw to think and to communicate.",
        "Not to document what you already built, in the week before delivery."),
    part("One", "Class diagrams"),
    svg("The structure of your game", UMLCLASS),
    table("Notation you actually need", ["Relationship", "Notation", "Means"], [
        ["Generalisation", "solid line, hollow triangle", "<code>extends</code> / <code>implements</code>"],
        ["Association", "solid line", "A knows about B"],
        ["Aggregation", "hollow diamond", "A has B; B survives A"],
        ["Composition", "filled diamond", "A has B; B dies with A"],
        ["Dependency", "dashed arrow", "A uses B transiently"],
    ]),
    two("Aggregation or composition?", "Aggregation &loz;", """
<p><code>Arena</code> &loz;&mdash; <code>Hero</code></p>
<p>The hero could exist in another arena. Destroy the arena, the hero is still a valid object.</p>""",
        "Composition &#9670;", """
<p><code>Hero</code> &#9670;&mdash; <code>Position</code></p>
<p>The position has no meaning without the hero. It is created and destroyed with it.</p>"""),
    bullets("Multiplicity", [
        "<code>1</code> &mdash; exactly one",
        "<code>0..1</code> &mdash; optional",
        "<code>*</code> or <code>0..*</code> &mdash; any number",
        "<code>1..*</code> &mdash; at least one",
        "Put it on both ends. &ldquo;<code>Arena 1 &mdash; * Element</code>&rdquo; says a lot in six characters.",
    ], tight=True),
    code("The diagram above, as code", "java", r"""
public abstract class Element {
    protected final Position position;      // composition
    public abstract void draw(GUI gui);
}

public class Hero extends Element { ... }   // generalisation
public class Wall extends Element { ... }
public class Monster extends Element { ... }

public class Arena {
    private final List<Element> elements;   // aggregation, 1 -- *
}
""", caption="If your diagram and your code disagree, the diagram is wrong."),
    q("What should <em>not</em> be on a class diagram?"),
    bullets("Leave it out", [
        "Every getter and setter",
        "Every field, when the point is the relationships",
        "Classes that are not part of the argument you are making",
        "<code>String</code>, <code>List</code>, and the rest of the JDK",
    ]),
    big("A diagram with forty boxes communicates nothing.",
        "Draw the six that matter for the point you are making."),
    part("Two", "Sequence diagrams"),
    q("A class diagram shows what exists. What shows what <em>happens</em>?"),
    svg("One keypress, end to end", SEQ),
    bullets("Reading it", [
        "Boxes at the top: objects, not classes &mdash; <code>:Arena</code>, not <code>Arena</code>",
        "Vertical dashed line: the lifeline. Time goes down.",
        "Thin rectangle: activation &mdash; this object is on the stack",
        "Solid arrow: a call. Dashed arrow: a return.",
        "Use it for the two or three interactions that are actually subtle",
    ]),
    big("Sequence diagrams are where you notice",
        "that your controller is talking to seven objects."),
    part("Three", "State diagrams"),
    q("Your game has a menu, a running state, a pause and a game-over screen. Where does that live in the code?"),
    svg("A state machine", STATE),
    bullets("Why draw it", [
        "It makes the illegal transitions visible &mdash; can you pause from the menu?",
        "Each state becomes a class (the State pattern, week 9)",
        "Each transition becomes a test",
        "The diagram <em>is</em> the test plan",
    ]),
    code("From diagram to tests", "java", r"""
@Test void escFromRunningPauses() {
    Game game = new Game(new RunningState(arena));
    game.processKey(ESC);
    assertInstanceOf(PausedState.class, game.state());
}

@Test void escFromMenuDoesNothing() {
    Game game = new Game(new MenuState());
    game.processKey(ESC);
    assertInstanceOf(MenuState.class, game.state());
}
"""),
    part("Practice", "Which diagram, when"),
    table("Three diagrams, three questions", ["Diagram", "Answers", "Use it when"], [
        ["Class", "What exists and how is it related?", "Arguing about structure &mdash; always"],
        ["Sequence", "Who calls whom, in what order?", "One interaction is subtle"],
        ["State", "What can happen next?", "An object has modes"],
    ]),
    bullets("Tooling", [
        "PlantUML or Mermaid &mdash; text, diffable, lives in the repository next to the code",
        "IntelliJ can generate a class diagram from your code &mdash; useful as a mirror, not as a design",
        "A photograph of a whiteboard is a perfectly good early design",
        "Do not spend an evening in a drawing tool. Spend it on the design.",
    ]),
    code("PlantUML, in your repo", "text", r"""
@startuml
abstract class Element {
  # position : Position
  + {abstract} draw(gui : GUI)
}
Element <|-- Hero
Element <|-- Wall
Arena "1" o-- "*" Element
Hero  *-- Position
@enduml
""", caption="<code>docs/design/model.puml</code> &mdash; reviewed in a pull request like any other file."),
    part("Project", "The assignment is out"),
    big("The project assignment is released today.",
        "Groups of three. A text-based game on Lanterna. Intermediate delivery in week 11."),
    bullets("Start with the diagram, not the game loop", [
        "Model the arena, the elements and the states before you write a line",
        "Bring that diagram to the lab next week &mdash; patterns will change it",
        "Groups are fixed this week; register them on Moodle",
        "The repository comes from the course template, with CI already wired",
    ]),
    lab("Lab 7", [
        "Draw the class diagram for your project's model, in PlantUML",
        "Draw the state machine for your game states",
        "Turn each transition into a JUnit test",
        "Review another group's diagram and find one relationship they got wrong",
    ]),
    takeaways([
        "Draw to decide, not to document",
        "Composition dies with the whole; aggregation does not",
        "Six boxes that make the argument beat forty that do not",
        "A state diagram is a test plan in disguise",
    ]),
]

# ================================================================== WEEK 08

W08 = [
    part("Design", "Patterns I"),
    q("Two groups solve the same problem, five years apart, and arrive at the same structure. What happened?"),
    big("The problem had a good solution.",
        "A pattern is that solution, written down and given a name."),
    bullets("What a pattern actually is", [
        "A <strong>name</strong> &mdash; so a design discussion fits in one word",
        "A <strong>problem</strong> &mdash; and the context where it appears",
        "A <strong>solution</strong> &mdash; a structure, not code you paste",
        "<strong>Consequences</strong> &mdash; what it costs you",
    ]),
    big("Gamma, Helm, Johnson, Vlissides. 1994.",
        "Twenty-three patterns, three families. Still the vocabulary of the profession."),
    table("The three families", ["Family", "Concerned with", "Examples"], [
        ["Creational", "How objects get made", "Factory Method, Abstract Factory, Builder, Singleton"],
        ["Structural", "How objects are composed", "Adapter, Composite, Decorator, Facade"],
        ["Behavioural", "How objects talk", "Strategy, Command, Observer, State, Iterator"],
    ]),
    big("A warning, before the catalogue.",
        "Patterns are answers. Learn the questions first, or you will apply them to problems you do not have."),
    part("Creational", "Making objects"),
    q("<code>new Monster()</code> is everywhere in your code. Why is that a problem?"),
    bullets("Because <code>new</code> is a commitment", [
        "It names a concrete class at every call site",
        "Change the class, edit every call site",
        "You cannot substitute a double in a test",
        "Creational patterns exist to move that decision to one place",
    ]),
    code("Factory Method", "java", r"""
abstract class LevelBuilder {
    protected abstract List<Monster> createMonsters();   // the factory method

    public Arena buildArena() {                          // the invariant algorithm
        Arena arena = new Arena(width(), height());
        arena.addAll(createWalls());
        arena.addAll(createMonsters());                  // subclass decides which
        return arena;
    }
}

class Level1Builder extends LevelBuilder {
    protected List<Monster> createMonsters() { return List.of(new Wanderer(...)); }
}
""", caption="The superclass owns the algorithm; the subclass owns the choice of class."),
    code("Abstract Factory", "java", r"""
interface ElementFactory {
    Hero    createHero(Position p);
    Monster createMonster(Position p);
    Wall    createWall(Position p);
}

class DungeonFactory implements ElementFactory { ... }
class ForestFactory  implements ElementFactory { ... }

// swap one object, and the whole family of elements changes theme
""", caption="Factory Method makes <em>one</em> product. Abstract Factory makes a consistent <em>family</em>."),
    code("Builder", "java", r"""
Arena arena = new Arena.Builder(20, 10)
        .withHero(new Position(1, 1))
        .withWalls(Wall.border())
        .withMonster(new Chaser(new Position(18, 8)))
        .build();
""", caption="Use it when a constructor has grown six parameters and four of them are optional."),
    q("Singleton. Who has used one?"),
    code("The pattern", "java", r"""
public final class GameConfig {
    private static final GameConfig INSTANCE = new GameConfig();
    private GameConfig() { }
    public static GameConfig getInstance() { return INSTANCE; }
}
"""),
    bullets("Why we will be strict about Singleton", [
        "It is global mutable state wearing a design pattern costume",
        "It hides dependencies &mdash; the signature does not say the class uses it",
        "It makes tests order-dependent, and it cannot be mocked",
        "In the project: using Singleton without a written justification <em>costs</em> marks",
        "Almost always, what you wanted was one instance <em>injected</em> in one place",
    ]),
    part("Structural", "Composing objects"),
    code("Adapter", "java", r"""
// You own this
public interface GUI {
    void drawHero(Position p);
    Action getNextAction();
}

// Lanterna owns this, and its shape is not yours
public class LanternaGUI implements GUI {
    private final Screen screen;

    public void drawHero(Position p) {
        TextGraphics g = screen.newTextGraphics();
        g.setForegroundColor(TextColor.Factory.fromString("#FFD700"));
        g.putString(p.x(), p.y(), "H");
    }
}
""", caption="The adapter is the single place in your project that knows Lanterna exists."),
    big("This one adapter is why your Model is testable.",
        "Everything on the other side of it can be mocked."),
    code("Composite", "java", r"""
interface MenuItem {
    void select();
    String label();
}

class Action implements MenuItem { ... }              // leaf

class Submenu implements MenuItem {                    // composite
    private final List<MenuItem> children = new ArrayList<>();
    public void select() { children.forEach(MenuItem::select); }
}
""", caption="Clients treat one item and a tree of items identically. That is the whole payoff."),
    code("Decorator", "java", r"""
interface Monster { Position nextPosition(Arena a); }

class Chaser implements Monster { ... }

class Poisoned implements Monster {            // wraps, same interface
    private final Monster inner;
    public Position nextPosition(Arena a) {
        damage(inner);
        return inner.nextPosition(a);
    }
}

new Poisoned(new Hasted(new Chaser(p)));       // stack behaviours at runtime
""", caption="Inheritance would need a class per combination. Decoration needs one per behaviour."),
    two("Decorator vs inheritance", "Inheritance", """
<ul><li>Fixed at compile time</li>
<li>N behaviours &rarr; 2<sup>N</sup> classes</li>
<li>Simple when there are two</li></ul>""",
        "Decorator", """
<ul><li>Composed at runtime</li>
<li>N behaviours &rarr; N classes</li>
<li>One more level of indirection to read</li></ul>"""),
    code("Facade", "java", r"""
public class Game {                      // the facade
    public void start() {
        gui.init();
        stateMachine.push(new MenuState());
        loop();
    }
}
// main() calls Game.start(). It does not know about screens,
// state machines, or the game loop.
"""),
    q("You have used at least three of these already this semester. Which?"),
    big("You have a project brief and a class diagram.",
        "This is the week the diagram changes."),
    bullets("What the report must justify", [
        "Every pattern you used, with the <em>problem</em> it solved",
        "A UML diagram of the part of the design that pattern shapes",
        "Patterns you considered and rejected &mdash; this scores as well as the ones you used",
        "A pattern applied without a problem is a code smell, and will be marked as one",
    ]),
    lab("Lab 8", [
        "Refactor the supplied game to introduce a <code>GUI</code> adapter",
        "Replace a growing <code>switch</code> on element type with a factory",
        "Find the Singleton in the supplied code and remove it",
    ]),
    takeaways([
        "A pattern is a name, a problem, a solution and a cost",
        "Factory Method: one product. Abstract Factory: a family.",
        "The adapter around Lanterna is the most valuable class in your project",
        "Singleton needs a justification, not a habit",
    ]),
]

# ================================================================== WEEK 09

W09 = [
    part("Design", "Patterns II"),
    big("Creational patterns make objects. Structural patterns arrange them.",
        "Behavioural patterns are about who talks to whom."),
    part("Strategy", "Interchangeable algorithms"),
    q("Three kinds of monster movement. Where does the choice live?"),
    code("Strategy", "java", r"""
interface MovementStrategy {
    Position nextPosition(Monster m, Arena a);
}

class ChasePlayer  implements MovementStrategy { ... }
class RandomWalk   implements MovementStrategy { ... }
class PatrolRoute  implements MovementStrategy { ... }

class Monster {
    private MovementStrategy movement;
    void setMovement(MovementStrategy m) { this.movement = m; }
    Position step(Arena a) { return movement.nextPosition(this, a); }
}
""", caption="Behaviour becomes a field. It can change at runtime &mdash; a monster that panics at low health."),
    big("Strategy is Open/Closed made concrete.",
        "You met the principle in week 6; this is what it looks like in the code."),
    part("Command", "Requests as objects"),
    q("What does it take to add undo to your game?"),
    code("Command", "java", r"""
interface Command {
    void execute();
    void undo();
}

class MoveHeroCommand implements Command {
    private final Arena arena;
    private final Direction direction;
    private Position previous;

    public void execute() {
        previous = arena.hero().position();
        arena.moveHero(direction);
    }
    public void undo() { arena.setHeroPosition(previous); }
}
"""),
    bullets("What you get once requests are objects", [
        "Undo and redo &mdash; keep a stack of them",
        "Key remapping &mdash; a <code>Map&lt;Key, Command&gt;</code>, configurable at runtime",
        "Macros &mdash; a command that holds a list of commands (Composite again)",
        "Replay and logging &mdash; the command history <em>is</em> the save file",
        "Testability &mdash; a command is trivially unit-testable in isolation",
    ]),
    big("Menus, keybindings and undo are the same problem.",
        "Command is why."),
    part("Observer", "One to many"),
    q("The score changes. Five things on screen need to know. How?"),
    code("Observer", "java", r"""
interface ScoreListener { void scoreChanged(int newScore); }

class Score {
    private final List<ScoreListener> listeners = new ArrayList<>();
    private int value;

    public void add(int points) {
        value += points;
        listeners.forEach(l -> l.scoreChanged(value));   // notify
    }
    public void addListener(ScoreListener l) { listeners.add(l); }
}
""", caption="The subject does not know what the listeners do. It only knows they exist."),
    bullets("Consequences", [
        "Subject and observers are loosely coupled &mdash; that is the point",
        "The order of notification is undefined. Do not depend on it.",
        "Cascading updates are hard to debug &mdash; a change can ripple",
        "Forgetting to unregister is a memory leak",
        "Every GUI framework you will ever use is built on this",
    ]),
    part("State", "An object with modes"),
    q("Week 7's state machine. How does it become code?"),
    code("State", "java", r"""
abstract class GameState {
    abstract GameState processKey(Key key, Game game);
    abstract void draw(GUI gui);
}

class RunningState extends GameState {
    GameState processKey(Key key, Game game) {
        if (key == ESC) return new PausedState(this);
        arena.moveHero(key.toDirection());
        return this;
    }
}

class PausedState extends GameState {
    private final GameState resumed;
    GameState processKey(Key key, Game game) {
        return key == ESC ? resumed : this;
    }
}
""", caption="No <code>switch (currentState)</code> anywhere. Each state knows only its own transitions."),
    two("State vs Strategy", "Same shape", """
<ul><li>Both delegate to an interface</li>
<li>Both replace a conditional</li>
<li>UML diagrams are near-identical</li></ul>""",
        "Different intent", """
<ul><li><strong>Strategy</strong>: the client picks. The object does not change itself.</li>
<li><strong>State</strong>: the object transitions itself, driven by events.</li></ul>"""),
    part("Two more", "Template Method &amp; Iterator"),
    code("Template Method", "java", r"""
abstract class Level {
    public final void load() {          // final: the algorithm is fixed
        createTerrain();
        placeHero();
        placeMonsters();                // subclasses fill in the steps
        placeItems();
    }
    protected abstract void placeMonsters();
    protected void placeItems() { }     // optional hook
}
""", caption="Factory Method is a Template Method whose step happens to create an object."),
    code("Iterator", "java", r"""
class Arena implements Iterable<Element> {
    private final List<Element> elements;
    public Iterator<Element> iterator() { return elements.iterator(); }
}

for (Element e : arena) { e.draw(gui); }
""", caption="Java gave you this one. Implement <code>Iterable</code> and the language cooperates."),
    part("Architecture", "Putting it together"),
    q("You have twelve classes and a game loop. Where does each one go?"),
    svg("Model &middot; View &middot; Controller", MVC),
    bullets("The three roles", [
        "<strong>Model</strong> &mdash; state and rules. Plain Java. No Lanterna, no keyboard, no screen.",
        "<strong>Viewer</strong> &mdash; reads the model and draws it. Holds no game state.",
        "<strong>Controller</strong> &mdash; takes input, changes the model, asks the viewer to redraw",
    ]),
    big("If the Model imports Lanterna, the design has failed.",
        "That single import is the difference between a testable project and an untestable one."),
    code("The game loop", "java", r"""
public void run() throws IOException {
    while (state != null) {
        gui.clear();
        state.draw(gui);
        gui.refresh();

        Action action = gui.getNextAction();
        if (action == Action.QUIT) break;
        state = state.step(this, action);       // State pattern
    }
    gui.close();
}
""", caption="Every pattern from this week is visible in twelve lines."),
    table("Where the patterns land in your project", ["Layer", "Typical patterns"], [
        ["Model", "State, Strategy, Composite, Observer"],
        ["Viewer", "Factory Method, Composite, Adapter"],
        ["Controller", "Command, State, Observer"],
        ["Boundary", "Adapter (Lanterna), Facade (Game)"],
    ]),
    q("How many patterns should the project use?"),
    big("As many as you have problems for.",
        "A report that lists nine patterns and justifies three scores worse than one that justifies three."),
    lab("Lab 9", [
        "Replace the game's state <code>switch</code> with the State pattern",
        "Add undo using Command",
        "Separate your Model from your Viewer; make the Model compile without Lanterna on the classpath",
    ]),
    takeaways([
        "Strategy: the client chooses. State: the object transitions.",
        "Command turns menus, keybindings, undo and replay into one mechanism",
        "Observer decouples, and makes debugging harder &mdash; both are true",
        "The Model must compile without the GUI. Test it by removing the dependency.",
    ]),
]
