#!/usr/bin/env python3
"""Weeks 10-13: Smells & refactoring · Mutation & PBT · Designing for change · Review & AI."""

from build import (big, bullets, code, lab, part, q, quote, svg, table,
                   takeaways, two)

MUTANT = """
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="14">
  <defs><marker id="u1" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
    <path d="M0 0 L9 4.5 L0 9 z" fill="#414a58"/></marker></defs>
  <rect x="40" y="112" width="150" height="60" rx="8" fill="none" stroke="#15181d" stroke-width="2.5"/>
  <text x="115" y="140" text-anchor="middle" font-weight="700" fill="#15181d">your code</text>
  <text x="115" y="160" text-anchor="middle" font-size="12" fill="#78828f">a &gt; b</text>
  <g fill="none" stroke="#a4161a" stroke-width="2.5">
    <rect x="300" y="26" width="160" height="50" rx="8"/>
    <rect x="300" y="118" width="160" height="50" rx="8"/>
    <rect x="300" y="210" width="160" height="50" rx="8"/>
  </g>
  <g text-anchor="middle" fill="#a4161a" font-family="SF Mono,Menlo,monospace" font-size="13">
    <text x="380" y="49">a &gt;= b</text><text x="380" y="66" font-size="11">mutant 1</text>
    <text x="380" y="141">a &lt; b</text><text x="380" y="158" font-size="11">mutant 2</text>
    <text x="380" y="233">true</text><text x="380" y="250" font-size="11">mutant 3</text>
  </g>
  <g stroke="#414a58" stroke-width="2" fill="none" marker-end="url(#u1)">
    <path d="M195 132 L295 55"/><path d="M195 142 L295 142"/><path d="M195 152 L295 228"/>
    <path d="M465 51 L560 51"/><path d="M465 143 L560 143"/><path d="M465 235 L560 235"/>
  </g>
  <g font-weight="700" font-size="15">
    <text x="572" y="57" fill="#1b6e46">killed &mdash; a test failed</text>
    <text x="572" y="149" fill="#1b6e46">killed &mdash; a test failed</text>
    <text x="572" y="241" fill="#a4161a">SURVIVED &mdash; all green</text>
  </g>
  <text x="380" y="292" text-anchor="middle" fill="#78828f" font-size="14">
    A survivor is a hole in your test suite, pointed at with a line number.</text>
</svg>
"""

# ================================================================== WEEK 10

W10 = [
    part("Quality", "Smells and refactoring"),
    q("Your project works and the tests are green. Is the code good?"),
    big("&ldquo;It works&rdquo; is not a quality standard.",
        "It is the entry requirement."),
    quote("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
          "Martin Fowler"),
    q("What is a code smell?"),
    big("A surface indication that usually corresponds to a deeper problem.",
        "Not a bug. Not always wrong. Always worth a second look."),
    part("The catalogue", "Smells you will find in your own project"),
    bullets("Bloaters", [
        "<strong>Long method</strong> &mdash; if you need a comment to explain a block, extract it",
        "<strong>Large class</strong> &mdash; too many fields, too many reasons to change",
        "<strong>Long parameter list</strong> &mdash; four or more; usually a missing object",
        "<strong>Primitive obsession</strong> &mdash; <code>int x, int y</code> everywhere instead of <code>Position</code>",
        "<strong>Data clumps</strong> &mdash; the same three values travelling together, always",
    ]),
    code("Primitive obsession, and its cure", "java", r"""
// before
void moveHero(int x, int y) { ... }
boolean isInside(int x, int y) { ... }
double distance(int x1, int y1, int x2, int y2) { ... }

// after
void moveHero(Position p) { ... }
boolean isInside(Position p) { ... }
double distance(Position a, Position b) { ... }
""", caption="You cannot pass a width where a height was expected once they have types."),
    bullets("Object-orientation abusers", [
        "<strong>Switch statements</strong> on type &mdash; polymorphism is asking to be used",
        "<strong>Refused bequest</strong> &mdash; a subclass that overrides parent methods to do nothing",
        "<strong>Temporary field</strong> &mdash; a field only set during one algorithm",
        "<strong>Alternative classes with different interfaces</strong> &mdash; same job, incompatible names",
    ]),
    bullets("Couplers", [
        "<strong>Feature envy</strong> &mdash; a method more interested in another class's data than its own",
        "<strong>Inappropriate intimacy</strong> &mdash; two classes that know each other's internals",
        "<strong>Message chains</strong> &mdash; <code>a.getB().getC().getD().doThing()</code>",
        "<strong>Middle man</strong> &mdash; a class that only delegates",
    ]),
    code("Feature envy", "java", r"""
// in class Renderer
void draw(Hero hero) {
    int x = hero.getPosition().getX();
    int y = hero.getPosition().getY();
    int hp = hero.getHealth();
    int max = hero.getMaxHealth();
    double ratio = (double) hp / max;      // this is Hero's business
    ...
}

// Hero should answer the question
double healthRatio() { return (double) health / maxHealth; }
""", caption="Move the behaviour to the data. That is what objects are for."),
    bullets("Dispensables", [
        "<strong>Duplicated code</strong> &mdash; the original sin; every other smell is downstream of it",
        "<strong>Dead code</strong> &mdash; delete it. Git remembers.",
        "<strong>Speculative generality</strong> &mdash; an abstraction for a requirement that never came",
        "<strong>Comments</strong> &mdash; sometimes deodorant sprayed on bad naming",
    ]),
    q("Are comments a smell?"),
    two("It depends on the comment", "Deodorant", """
<pre><code class="language-java">// check if hero is alive and
// has not left the arena
if (h.hp > 0 && a.in(h.p)) {</code></pre>
<p>Extract a well-named method instead.</p>""",
        "Valuable", """
<pre><code class="language-java">// Lanterna reports the terminal size
// one row short on macOS; see #142
height = terminal.getRows() + 1;</code></pre>
<p>Explains <em>why</em>. The code cannot.</p>"""),
    part("The cure", "Refactoring"),
    big("Refactoring: changing the internal structure",
        "without changing the observable behaviour."),
    big("Without a test suite, it is not refactoring.",
        "It is just editing and hoping."),
    bullets("The discipline", [
        "Start green",
        "Make one small transformation",
        "Run the tests",
        "Commit",
        "Repeat. If you are ever more than five minutes from green, back out.",
    ]),
    table("Refactorings worth knowing by name", ["Refactoring", "Applies to"], [
        ["Extract Method", "Long method, duplicated code, comments"],
        ["Extract Class", "Large class, data clumps"],
        ["Introduce Parameter Object", "Long parameter list, primitive obsession"],
        ["Move Method / Move Field", "Feature envy, inappropriate intimacy"],
        ["Replace Conditional with Polymorphism", "Switch on type"],
        ["Replace Magic Number with Constant", "Unexplained literals"],
        ["Rename", "Everything. The most valuable and most neglected."],
    ]),
    code("Replace conditional with polymorphism", "java", r"""
// before
int damage(Monster m) {
    switch (m.getType()) {
        case CHASER:  return 10;
        case FLYER:   return 5;
        case BOSS:    return 30;
        default:      return 0;
    }
}

// after
interface Monster { int damage(); }
class Chaser implements Monster { public int damage() { return 10; } }
class Boss   implements Monster { public int damage() { return 30; } }
""", caption="Adding a monster now touches zero existing files."),
    big("Your IDE does most of this for you.",
        "Rename, Extract Method, Introduce Parameter, Change Signature &mdash; learn the four shortcuts."),
    q("When do you refactor?"),
    bullets("Three good moments, one bad one", [
        "<strong>Before</strong> adding a feature &mdash; make the change easy, then make the easy change",
        "<strong>After</strong> getting it green &mdash; the third step of TDD",
        "<strong>When you read it</strong> and had to think twice",
        "<strong>Not</strong> as a two-week &ldquo;refactoring sprint&rdquo; with the suite red",
    ]),
    part("Measuring", "Static analysis"),
    bullets("Tools that find smells for you", [
        "<strong>SonarQube / SonarCloud</strong> &mdash; smells, duplication, complexity, coverage in one report",
        "<strong>PMD</strong> &mdash; rule-based; good at long methods and dead code",
        "<strong>SpotBugs</strong> &mdash; bytecode analysis; finds real bugs, not just style",
        "<strong>IntelliJ inspections</strong> &mdash; already running, already ignored",
    ]),
    big("The report asks which smells remain in your code.",
        "&ldquo;None&rdquo; is not a credible answer. Knowing which ones, and why you left them, is."),
    lab("Lab 10", [
        "Run SonarCloud or PMD on your project; read the top twenty findings",
        "Pick the worst method and refactor it in five commits, green at each step",
        "Replace one switch-on-type with polymorphism",
        "Write down three smells you are choosing to keep, and why",
    ]),
    takeaways([
        "A smell is a hint, not a verdict",
        "Move behaviour to the data it uses",
        "Refactoring without tests is editing and hoping",
        "Small steps, green at every commit",
    ]),
]

# ================================================================== WEEK 11

W11 = [
    part("Quality", "How good are your tests?"),
    q("Your suite has 92% branch coverage. How many bugs would it catch?"),
    big("Coverage tells you what was executed.",
        "It says nothing about what was <em>checked</em>."),
    code("92% coverage, zero verification", "java", r"""
@Test
void gameRuns() {
    Game game = new Game(new Arena(20, 10));
    game.step(Action.UP);
    game.step(Action.DOWN);
    game.step(Action.LEFT);
}
// green, high coverage, and it would pass if step() did nothing at all
"""),
    q("So how do you test the tests?"),
    big("Break the code on purpose.",
        "If the suite stays green, the suite is not doing its job."),
    part("Mutation testing", "Fault injection, automated"),
    svg("The idea", MUTANT),
    bullets("How it runs", [
        "The tool makes small changes to your bytecode &mdash; <em>mutants</em>",
        "For each mutant, it runs the tests that cover that line",
        "Test fails &rarr; the mutant is <strong>killed</strong>. Good.",
        "All green &rarr; the mutant <strong>survived</strong>. Your suite missed it.",
        "<em>Mutation score</em> = killed / total",
    ]),
    table("Typical mutation operators", ["Operator", "Example"], [
        ["Conditionals boundary", "<code>a &gt; b</code> &rarr; <code>a &gt;= b</code>"],
        ["Negate conditionals", "<code>a == b</code> &rarr; <code>a != b</code>"],
        ["Math", "<code>a + b</code> &rarr; <code>a - b</code>"],
        ["Increments", "<code>i++</code> &rarr; <code>i--</code>"],
        ["Void method calls", "remove the call entirely"],
        ["Return values", "<code>return x</code> &rarr; <code>return null</code>"],
    ]),
    code("PIT in the Gradle build", "kotlin", r"""
plugins { id("info.solidsoft.pitest") version "1.15.0" }

pitest {
    junit5PluginVersion = "1.2.1"
    targetClasses = setOf("com.ldts.game.model.*")
    mutators = setOf("STRONGER")
    timestampedReports = false
    mutationThreshold = 70          // fail the build below this
}
""", caption="<code>./gradlew pitest</code> &rarr; <code>build/reports/pitest/index.html</code>"),
    big("Read the surviving mutants, not the score.",
        "Each survivor is a line number and a missing assertion."),
    bullets("What survivors usually mean", [
        "You executed the line but asserted nothing about its effect",
        "You asserted on the wrong thing &mdash; a count instead of a value",
        "The mutated code is genuinely equivalent (rare, and worth writing down)",
        "The line is dead and should be deleted",
    ]),
    bullets("Cost and how to live with it", [
        "It is slow &mdash; every mutant is a test run",
        "Target the <em>model</em> package only; do not mutate the Lanterna adapter",
        "Run it nightly on CI, not on every push",
        "In the project: a mutation report is required. A score above 70% on the model is the bar.",
    ]),
    part("Property-based testing", "Stop inventing examples"),
    q("How many example tests would it take to be confident in <code>Position.translate</code>?"),
    big("Example tests check the cases you thought of.",
        "That is precisely the set that excludes your bugs."),
    bullets("The shift", [
        "Stop writing: for input 3, expect 4",
        "Start writing: for <em>all</em> inputs, this property holds",
        "The framework generates hundreds of inputs, including the nasty ones",
        "When it fails, it <em>shrinks</em> the input to the smallest failing case",
    ]),
    code("A property, with jqwik", "java", r"""
import net.jqwik.api.*;

class PositionProperties {

    @Property
    void translateThenBackIsIdentity(@ForAll int x, @ForAll int y,
                                     @ForAll @IntRange(min=-50, max=50) int dx,
                                     @ForAll @IntRange(min=-50, max=50) int dy) {
        Position start = new Position(x, y);

        Position there = start.translate(dx, dy);
        Position back  = there.translate(-dx, -dy);

        assertThat(back).isEqualTo(start);
    }
}
""", caption="jqwik is a JUnit 5 engine. Same build, same <code>./gradlew test</code>, no new language."),
    code("Constraining the domain", "java", r"""
@Property
void heroNeverLeavesArena(@ForAll("arenas") Arena arena,
                          @ForAll Direction direction) {
    arena.moveHero(direction);
    assertTrue(arena.isInside(arena.hero().position()));
}

@Provide
Arbitrary<Arena> arenas() {
    return Combinators.combine(
            Arbitraries.integers().between(3, 40),
            Arbitraries.integers().between(3, 40))
        .as(Arena::new);
}
""", caption="This one property replaces about twenty example tests &mdash; and finds the corner you forgot."),
    bullets("Properties worth looking for", [
        "<strong>Round trip</strong> &mdash; encode then decode returns the original",
        "<strong>Invariant</strong> &mdash; something that is true after every operation",
        "<strong>Idempotence</strong> &mdash; doing it twice is the same as once",
        "<strong>Commutativity</strong> &mdash; order does not matter",
        "<strong>Oracle</strong> &mdash; agrees with a slow, obviously-correct implementation",
    ]),
    two("Two kinds of test, both needed", "Example", """
<ul><li>Documents one concrete behaviour</li>
<li>Readable as a specification</li>
<li>Fast, deterministic</li>
<li>Only finds what you predicted</li></ul>""",
        "Property", """
<ul><li>Documents a general rule</li>
<li>Explores inputs you would not</li>
<li>Shrinks failures automatically</li>
<li>Harder to write; some code has no obvious properties</li></ul>"""),
    big("Coverage &rarr; mutation score &rarr; properties.",
        "Three increasingly honest answers to &ldquo;are my tests any good?&rdquo;"),
    bullets("Intermediate delivery is this week", [
        "Design so far: class diagram, patterns used, with justification",
        "A running game, however small",
        "Coverage and mutation reports, with the numbers as they actually are",
        "15% of the project grade &mdash; and the last cheap moment to change direction",
    ]),
    part("Assessment", "Test #2 is this week"),
    bullets("Format", [
        "In the PC rooms, IntelliJ open, 75 minutes, individual",
        "A small repository is handed to you, with a failing behaviour",
        "Tasks: write a test that exposes the bug; fix it; refactor one named smell",
        "Graded by a hidden test suite plus a rubric on the refactoring",
        "No assistants, no internet. Javadoc is available locally.",
        "20% of the final grade",
    ]),
    bullets("How to prepare", [
        "Practise the IntelliJ refactoring shortcuts until they are automatic",
        "Be able to write a JUnit 5 test from memory, including <code>assertThrows</code>",
        "Be able to read a JaCoCo report and say what is missing",
        "Redo Labs 3, 4 and 10 under time pressure",
    ]),
    lab("Lab 11", [
        "Add PIT to your build; run it on the model package",
        "Take the three highest-value survivors and kill them",
        "Write two properties for your model with jqwik",
        "Compare: what did the properties find that your examples did not?",
    ]),
    takeaways([
        "Coverage measures execution; mutation testing measures verification",
        "A surviving mutant is a missing assertion with a line number",
        "Properties test rules, examples test cases &mdash; write both",
        "Target mutation at the model, not at the adapter",
    ]),
]

# ================================================================== WEEK 12

W12 = [
    part("Project", "Designing for change"),
    q("Which is the better design: the elegant one, or the one that absorbs next week's requirement?"),
    big("Nobody can tell you a design is good by looking at it.",
        "You find out when the requirement changes."),
    quote("Make the change easy, then make the easy change. Warning: the first part is often hard.",
          "Kent Beck"),
    part("One", "Demos"),
    big("Every group demos today.",
        "Ten minutes: play it, then defend the design behind it."),
    bullets("The demo format", [
        "Five minutes playing the game &mdash; features as they actually are, not as planned",
        "Five minutes on the design: class diagram, the patterns, one thing you regret",
        "Another group reviews you against the checklist below",
        "You are graded on the review you give as well as the demo you present",
        "Bring the coverage and mutation numbers. Real ones.",
    ]),
    bullets("The critique checklist", [
        "Is each pattern <em>justified</em> by a problem, or applied because it was on the list?",
        "Does the class diagram match the code? (Check one class at random.)",
        "Where is the game loop? What does it know about?",
        "What breaks if the terminal library is replaced?",
        "What is the least-tested class, and is that a deliberate choice?",
        "Which single change would most improve this design?",
    ]),
    part("Two", "The requirement drop"),
    big("A new requirement, announced now.",
        "It is worth 10% of the project grade, and you have two weeks."),
    bullets("What is being measured", [
        "Not whether you implement it &mdash; most groups will",
        "<strong>How much existing code you had to modify</strong>",
        "How many tests broke that should not have",
        "Whether the abstractions you argued for in week 11 actually paid off",
        "Your commit history is the evidence",
    ]),
    big("This is the Open/Closed principle being marked.",
        "A design that only needs new files scores highest."),
    bullets("How to approach it", [
        "Before writing anything: sketch which classes must change, and why",
        "If the answer is &ldquo;most of them&rdquo;, refactor first, then add the feature",
        "Run the suite before you start. Note which tests break as you go.",
        "A test that breaks because behaviour changed is fine. One that breaks because a constructor moved is a design smell.",
    ]),
    part("Diagnosis", "Reading your own design"),
    q("How do you tell, before the change lands, whether your design will absorb it?"),
    bullets("Questions to ask of your own code", [
        "How many files does a new monster type touch? A new input device? A new renderer?",
        "Can the model be compiled with Lanterna off the classpath?",
        "Is there any <code>switch</code> or <code>instanceof</code> on a type you own?",
        "Which class has the most incoming dependencies? Is that deliberate?",
        "How long is the longest method, honestly?",
    ]),
    table("Coupling and cohesion, in practice", ["", "Bad sign", "Good sign"], [
        ["Coupling", "Class knows another's fields, order of calls, or concrete type",
         "Talks through an interface it owns"],
        ["Cohesion", "Methods share no fields; the class is a bag of functions",
         "Every method uses the state"],
        ["Direction", "Model imports the GUI", "GUI imports the model"],
    ]),
    big("Dependencies should point towards stability.",
        "The rules of your game change less often than the way you draw them. Point the arrows accordingly."),
    q("&ldquo;We would design it completely differently if we started again.&rdquo;"),
    big("That sentence is the learning outcome.",
        "Write it in the report, with what you would do instead."),
    part("Ahead", "The last week"),
    bullets("What remains", [
        "Week 13: code review and AI-assisted development",
        "Final delivery: code, report, and the individual defence",
        "The defence asks about <em>your</em> commits &mdash; look at them before you come",
    ]),
    bullets("Report: the sections that carry the marks", [
        "Implemented features, with screenshots",
        "Design: the problem, the pattern, the alternative you rejected, the UML",
        "Code smells that remain, and why",
        "Testing: coverage, mutation score, one property you are proud of",
        "Self-evaluation, per member, that the group agrees on",
    ]),
    lab("Lab 12", [
        "Demo your game; review another group's design",
        "Plan the requirement drop: which classes change, which are only added",
        "Refactor first if the plan says &ldquo;change&rdquo; more than &ldquo;add&rdquo;",
    ]),
    takeaways([
        "A design is judged by the cost of the next change",
        "New behaviour should mean new files",
        "Dependencies point towards what changes least",
        "Being able to critique your own design is the skill being assessed",
    ]),
]

# ================================================================== WEEK 13

W13 = [
    part("Practice", "Review, assistants, and what comes next"),
    part("One", "Code review"),
    q("Your teammate opens a pull request with 400 changed lines. What do you do?"),
    big("Send it back.",
        "A review of 400 lines finds style errors. A review of 40 finds bugs."),
    bullets("What a reviewer is actually for", [
        "Finding defects &mdash; the original purpose, and still the cheapest place to find them",
        "Spreading knowledge &mdash; two people now understand that code",
        "Keeping the design coherent &mdash; the only checkpoint before it is merged",
        "Not: checking formatting. A tool does that.",
    ]),
    bullets("How to review", [
        "Read the description first. If there is none, that is the first comment.",
        "Understand the <em>intent</em> before judging the implementation",
        "Ask questions rather than issuing verdicts: &ldquo;what happens if this is empty?&rdquo;",
        "Distinguish blocking problems from preferences, and say which is which",
        "Approve when it is better than what is on <code>main</code> &mdash; not when it is perfect",
    ]),
    two("Two comments", "Unhelpful", """
<pre><code class="language-text">this is wrong

why did you do it like this?

nit: nit: nit: nit: nit:</code></pre>""",
        "Helpful", """
<pre><code class="language-text">Blocking: if elements is empty this
throws. Test with an empty arena?

Suggestion (non-blocking): this reads
like Feature Envy - could damage()
live on Monster?</code></pre>"""),
    bullets("Receiving a review", [
        "The code is being reviewed, not you",
        "Every comment gets a response &mdash; changed, or explained",
        "&ldquo;Good catch&rdquo; is a complete and sufficient reply",
        "If you disagree, say why. A reviewer can be wrong.",
    ]),
    part("Two", "AI assistants"),
    q("You have all used one this semester. Let us talk about it properly."),
    big("The generation problem is largely solved.",
        "The verification problem is entirely yours."),
    bullets("What assistants are genuinely good at", [
        "Boilerplate: builders, <code>equals</code>, adapters, test scaffolding",
        "Explaining unfamiliar APIs and error messages",
        "First-draft tests for a method you already designed",
        "Suggesting the name of a pattern you have half-described",
    ]),
    bullets("Where they reliably fail", [
        "Design decisions that depend on <em>your</em> constraints",
        "Tests that assert something meaningful rather than something true",
        "Knowing that a pattern is unnecessary here",
        "Being wrong confidently, in code that compiles and passes",
    ]),
    code("Generated, plausible, worthless", "java", r"""
@Test
void testMoveHero() {
    Arena arena = new Arena(10, 10);
    arena.moveHero(Direction.UP);
    assertNotNull(arena.getHero());     // true before the call, too
}
""", caption="Compiles. Passes. Adds coverage. Kills no mutants. This is the failure mode to recognise."),
    bullets("The habit to build", [
        "Never accept code you could not have written",
        "Ask it for the test, then check the test would fail against broken code",
        "Run mutation testing on generated tests &mdash; it exposes them immediately",
        "Treat every suggestion as a pull request from a fast, confident, junior colleague",
    ]),
    big("Review is the skill that transfers.",
        "It was valuable before assistants. It is now the whole job."),
    bullets("For the report and the defence", [
        "Declare where you used assistance and for what",
        "You own every line, including the ones you did not type",
        "At the defence you will be asked to explain a class you did not write by hand. Read your own code first.",
        "This is not a trap. It is what code review is in any team you will join.",
    ]),
    part("Three", "Closing"),
    table("What you learned, by verb", ["", "Week", "Now you can"], [
        ["Design", "6&ndash;9", "Justify a structure, name the pattern, defend the trade-off"],
        ["Test", "3&ndash;5, 11", "Write tests that would fail if the code were wrong"],
        ["Refactor", "10, 12", "Change structure without changing behaviour"],
        ["Collaborate", "1, 13", "Work through branches, pull requests and review"],
    ]),
    q("What is the one thing to keep from this course?"),
    big("Code is read far more often than it is written,",
        "and changed far more often than it is read."),
    bullets("Where this goes next in L.EIC", [
        "<strong>ESOF</strong> &mdash; process, requirements, teams at scale",
        "<strong>LPOO / LBAW</strong> &mdash; the same design ideas in other domains",
        "Everything you build for the rest of the degree",
    ]),
    bullets("If you want to go further", [
        "Freeman &amp; Pryce, <em>Growing Object-Oriented Software, Guided by Tests</em>",
        "Fowler, <em>Refactoring</em> (2nd ed.) &mdash; work through the catalogue",
        "Ousterhout, <em>A Philosophy of Software Design</em> &mdash; short, and disagrees with Fowler in useful ways",
        "Read a real codebase. Pick one you use and read its tests first.",
    ]),
    big("Final delivery and defences follow.",
        "Bring your commit history. Thank you &mdash; it was a good semester."),
    takeaways([
        "Small pull requests get real reviews",
        "Assistants generate; you verify. The second half is the job.",
        "A test that cannot fail is not a test",
        "Design is judged by the cost of the next change",
    ]),
]
