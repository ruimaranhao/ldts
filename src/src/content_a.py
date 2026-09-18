#!/usr/bin/env python3
"""Weeks 1-4: Git · Java & Gradle · Test automation · Testing strategies."""

from build import (big, bullets, code, lab, part, q, quote, svg, table,
                   takeaways, takeaways as _t, two)

# ---------------------------------------------------------------- SVG figures

TREES = """
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="15">
  <g fill="none" stroke="#414a58" stroke-width="2">
    <rect x="20"  y="60" width="180" height="90" rx="8"/>
    <rect x="290" y="60" width="180" height="90" rx="8"/>
    <rect x="560" y="60" width="180" height="90" rx="8"/>
  </g>
  <g fill="#15181d" text-anchor="middle" font-weight="700">
    <text x="110" y="100">working</text><text x="110" y="120">directory</text>
    <text x="380" y="100">staging area</text><text x="380" y="120">(index)</text>
    <text x="650" y="100">repository</text><text x="650" y="120">(HEAD)</text>
  </g>
  <g stroke="#a4161a" stroke-width="2.5" fill="none" marker-end="url(#ar)">
    <path d="M205 95 L285 95"/><path d="M475 95 L555 95"/>
  </g>
  <g stroke="#1d4e89" stroke-width="2.5" fill="none" marker-end="url(#ab)">
    <path d="M555 135 L475 135"/><path d="M285 135 L205 135"/>
  </g>
  <defs>
    <marker id="ar" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
      <path d="M0 0 L9 4.5 L0 9 z" fill="#a4161a"/></marker>
    <marker id="ab" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
      <path d="M0 0 L9 4.5 L0 9 z" fill="#1d4e89"/></marker>
  </defs>
  <g fill="#a4161a" text-anchor="middle" font-size="13" font-weight="700">
    <text x="245" y="86">git add</text><text x="515" y="86">git commit</text>
  </g>
  <g fill="#1d4e89" text-anchor="middle" font-size="13" font-weight="700">
    <text x="515" y="158">git reset</text><text x="245" y="158">git checkout --</text>
  </g>
  <text x="380" y="215" text-anchor="middle" fill="#78828f" font-size="14">
    Every command you will ever type moves something between these three places.</text>
</svg>
"""

BRANCH = """
<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="14">
  <line x1="60" y1="170" x2="700" y2="170" stroke="#c9c4ba" stroke-width="2"/>
  <g stroke="#15181d" stroke-width="2.5" fill="none">
    <path d="M100 170 L250 170"/><path d="M430 170 L700 170"/>
  </g>
  <path d="M250 170 C300 170 300 80 350 80 L470 80 C520 80 520 170 570 170"
        stroke="#a4161a" stroke-width="2.5" fill="none"/>
  <g fill="#15181d">
    <circle cx="100" cy="170" r="9"/><circle cx="175" cy="170" r="9"/>
    <circle cx="250" cy="170" r="9"/><circle cx="490" cy="170" r="9"/>
    <circle cx="570" cy="170" r="11" fill="#1d4e89"/><circle cx="660" cy="170" r="9"/>
  </g>
  <g fill="#a4161a">
    <circle cx="350" cy="80" r="9"/><circle cx="410" cy="80" r="9"/>
    <circle cx="470" cy="80" r="9"/>
  </g>
  <text x="80"  y="205" fill="#15181d" font-weight="700">main</text>
  <text x="330" y="58"  fill="#a4161a" font-weight="700">feature/rendering</text>
  <text x="545" y="205" fill="#1d4e89" font-weight="700">merge</text>
  <text x="380" y="228" text-anchor="middle" fill="#78828f">
    A branch is a movable pointer to a commit. That is the whole idea.</text>
</svg>
"""

CFG = """
<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica,Arial" font-size="15">
  <defs><marker id="a2" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto">
    <path d="M0 0 L9 4.5 L0 9 z" fill="#414a58"/></marker></defs>
  <g stroke="#414a58" stroke-width="2" fill="none" marker-end="url(#a2)">
    <path d="M380 48 L380 76"/><path d="M370 108 L300 136"/><path d="M390 108 L460 136"/>
    <path d="M300 168 L370 196"/><path d="M460 168 L390 196"/><path d="M380 228 L380 254"/>
  </g>
  <g fill="none" stroke="#15181d" stroke-width="2.5">
    <rect x="320" y="18"  width="120" height="30" rx="6"/>
    <rect x="240" y="196" width="280" height="32" rx="6"/>
    <rect x="320" y="254" width="120" height="30" rx="6"/>
    <rect x="228" y="136" width="144" height="32" rx="6"/>
    <rect x="400" y="136" width="144" height="32" rx="6"/>
  </g>
  <path d="M380 76 L424 92 L380 108 L336 92 z" fill="none" stroke="#a4161a" stroke-width="2.5"/>
  <g fill="#15181d" text-anchor="middle" font-family="SF Mono,Menlo,monospace" font-size="14">
    <text x="380" y="38">f1();</text>
    <text x="380" y="97" fill="#a4161a">b1</text>
    <text x="300" y="157">f2();</text>
    <text x="472" y="157">skip</text>
    <text x="380" y="217">f3();</text>
    <text x="380" y="274">f5();</text>
  </g>
  <g fill="#78828f" font-size="13">
    <text x="326" y="128">true</text><text x="404" y="128">false</text>
  </g>
</svg>
"""

# ================================================================== WEEK 01

W01 = [
    part("Part one", "What this course is"),
    q("You can already write a program that works.",
      "So what is left to learn?"),
    big("Making it work is the easy part.",
        "Making it survive six months of change is the course."),
    bullets("By January you should be able to", [
        "Design an object-oriented system and <em>justify</em> the design",
        "Write tests that would actually catch a regression",
        "Read a class and name what is wrong with it",
        "Refactor without breaking behaviour",
        "Work in a team through Git, not through a zip file",
    ], kicker="Learning outcomes"),
    big("Design &middot; Test &middot; Refactor",
        "The three verbs. Everything in the syllabus is one of them."),
    table("The 13 weeks", ["", "Topic", "Block"], [
        ["1", "Git &amp; GitHub", "Foundations"],
        ["2", "Java &amp; Gradle", "Foundations"],
        ["3", "Test automation, V&amp;V, JUnit 5", "Testing"],
        ["4", "Testing strategies &amp; coverage", "Testing"],
        ["5", "Test doubles, test-first, CI", "Testing"],
        ["6", "SOLID principles &nbsp;<strong>&larr; test #1</strong>", "Design"],
        ["7", "UML for design &nbsp;<strong>&larr; project out</strong>", "Design"],
        ["8", "Patterns I &mdash; creational &amp; structural", "Design"],
        ["9", "Patterns II &mdash; behavioural, MVC", "Design"],
        ["10", "Code smells &amp; refactoring", "Quality"],
        ["11", "Mutation &amp; property-based testing &nbsp;<strong>&larr; test #2</strong>", "Quality"],
        ["12", "Demos &amp; the requirement drop", "Project"],
        ["13", "Code review, AI-assisted development", "Project"],
    ], kicker="Master plan"),
    part("Part two", "How you are assessed"),
    table("Assessment", ["Component", "Weight", "Kind"], [
        ["Project", "55%", "Group of 3 (same practical class), might include individual defence"],
        ["Test #1 (week 6)", "20%", "Individual, multiple choice"],
        ["Test #2 (week 11)", "20%", "Individual, assignment or multiple choice"],
        ["Participation", "5%", "Individual"],
    ]),
    big("Minimum 40% in every component.",
        "A brilliant project cannot rescue a blank test."),
    bullets("The project, in one slide", [
        "A text-based game in Java, on top of Lanterna",
        "Groups of exactly three",
        "Two deliveries: intermediate (design) and final",
        "Graded on <em>design</em>, not on how many features you shipped",
        "The final delivery might include an individual defence",
    ]),
    q("Why a game?"),
    big("Because a game changes.",
        "New enemy, new input, new renderer. Rigid designs die visibly."),
    bullets("Rules that bite", [
        "Frequency: you may not exceed the allowed absences",
        "All deliveries on the announced date &mdash; no exceptions negotiated by email",
        "Only the written tests can be retaken for improvement",
        "Plagiarism between groups is an academic offence, and it is easy to detect",
    ]),
    part("Part three", "AI assistants"),
    q("Will you use Copilot on the project?",
      "Yes. So let us be explicit about it."),
    bullets("The policy", [
        "AI assistance is <strong>allowed</strong> and expected",
        "You must declare it: a short section in the report saying where and how",
        "You are responsible for every line you submit &mdash; including the ones you did not type",
        "At the defence you will be asked to explain <em>your</em> code. &ldquo;The model wrote it&rdquo; is not an answer",
        "Tests #1 and #2 are closed-assistant &mdash; no internet, no models",
    ]),
    big("The skill being assessed is judgement.",
        "Generating code is now cheap. Knowing whether it is any good is not."),
    bullets("Who we are", [
        "Rui Maranhão",
        "Sofia Reis",
        "André Restivo",
        "Auri Vincenzi",
        "Rui Melo",
        "Nuno Flores",
        "Lázaro Costa",
        "Cláudia Mamede",
    ], kicker="Teaching team", tight=True),
    bullets("Where to find us", [
        "<strong>Office hours</strong> &mdash; times and rooms are on Moodle; book before you show up",
        "<strong>Slack</strong> &mdash; for everything else, and faster than email",
        "Ask early. A question in week 12 about a week 6 idea is an expensive question.",
    ]),
    bullets("Books", [
        "<strong>Bloch</strong>, <em>Effective Java</em> (3rd ed.) &mdash; the one to actually own",
        "<strong>Fowler</strong>, <em>Refactoring</em> (2nd ed.)",
        "<strong>Freeman &amp; Robson</strong>, <em>Head First Design Patterns</em>",
        "<strong>Gamma et al.</strong>, <em>Design Patterns</em> &mdash; reference, not bedtime reading",
        "<strong>Miles &amp; Hamilton</strong>, <em>Learning UML 2.0</em>",
    ]),
    part("Part four", "Git"),
    q("Why does version control exist?"),
    big("Because you will break things.",
        "And because three people will break them at the same time."),
    bullets("What Git actually gives you", [
        "A way back to any state the code has ever been in",
        "A record of <em>who</em> changed <em>what</em> and <em>why</em>",
        "Parallel lines of work that can be recombined",
        "In this course: the evidence of who did what in your group",
    ]),
    svg("The three trees", TREES,
        caption="Everything else is convenience on top of this."),
    code("The loop you will run a thousand times", "bash", r"""
git status                  # what changed, what is staged
git add src/Hero.java       # move changes into the staging area
git commit -m "Add Hero movement bounds"
git push origin main
""", kicker="Daily"),
    q("Why is there a staging area at all?",
      "Why not just commit everything that changed?"),
    big("Because a commit should be one idea.",
        "Staging is what lets you split three hours of work into four honest commits."),
    svg("Branching", BRANCH),
    code("Feature branches", "bash", r"""
git switch -c feature/rendering   # create and switch (modern form)
# ... work, commit, commit ...
git switch main
git merge feature/rendering
""", caption="<code>git checkout -b</code> still works; <code>switch</code> is clearer."),
    two("Merge or rebase?", "merge", """
<ul><li>Keeps the true history</li>
<li>Creates a merge commit</li>
<li>Safe on shared branches</li></ul>""",
        "rebase", """
<ul><li>Replays your commits on a new base</li>
<li>Linear, readable history</li>
<li><strong>Never</strong> rebase a branch someone else has pulled</li></ul>"""),
    q("A conflict appears. What has actually gone wrong?"),
    big("Nothing.",
        "Git is telling you two humans edited the same lines and it will not guess."),
    code("Resolving", "bash", r"""
git merge feature/rendering
# CONFLICT (content): Merge conflict in src/Arena.java

# open the file, keep what should survive, delete the markers
git add src/Arena.java
git commit
""", kicker="Conflicts"),
    big("Commit messages are documentation.",
        "In six weeks you will read them to find out when the bug got in."),
    two("Two commit messages", "Useless", """
<pre><code class="language-text">fix
stuff
final version
final version 2
asdasd</code></pre>""",
        "Useful", """
<pre><code class="language-text">Clamp hero position to arena bounds

Hero could walk through the right wall when
the arena width was odd. Off-by-one in
Arena.isInside.</code></pre>"""),
    q("Git or GitHub?"),
    bullets("They are not the same thing", [
        "<strong>Git</strong> &mdash; the version control system. Runs on your machine. Works offline.",
        "<strong>GitHub</strong> &mdash; a hosting service with a social layer on top of Git",
        "Pull requests, issues, code review, Actions: GitHub, not Git",
        "You could do this whole course with Git and no GitHub. You would just enjoy it less.",
    ]),
    bullets("The workflow we use", [
        "One repository per group, created from the course template",
        "<code>main</code> is always green &mdash; it builds and the tests pass",
        "Work happens on branches, arrives through pull requests",
        "Every pull request is reviewed by a teammate before it is merged",
        "Your commit history <em>is</em> part of the project grade",
    ]),
    lab("Lab 1", [
        "Set up Git, SSH keys and your IDE",
        "Clone the course repository, create a branch, open a pull request",
        "Deliberately create a conflict with your partner and resolve it",
        "Rewrite five bad commit messages from a sample repository",
    ]),
    takeaways([
        "A commit is one idea; the staging area is what makes that possible",
        "A branch is a pointer, not a copy",
        "<code>main</code> is always green",
        "History is evidence &mdash; in this course it is graded evidence",
    ]),
]

# ================================================================== WEEK 02

W02 = [
    part("Part one", "Java, for people who already program"),
    q("You know C and C++. What is genuinely different here?"),
    table("The short version", ["", "C++", "Java"], [
        ["Memory", "You free it", "Garbage collected"],
        ["Compilation", "To machine code", "To bytecode, then JIT"],
        ["Inheritance", "Multiple", "Single, plus many interfaces"],
        ["Pointers", "Yes, arithmetic and all", "References only, no arithmetic"],
        ["Generics", "Templates, compile-time expansion", "Erasure &mdash; type info is gone at runtime"],
        ["Header files", "Yes", "No"],
    ]),
    big("There are only two kinds of value in Java.",
        "Primitives, and references to objects. Everything follows from that."),
    code("Primitives and references", "java", r"""
int a = 5;              // a *is* 5
int b = a;              // b is a copy

int[] xs = {1, 2, 3};   // xs is a *reference* to an array
int[] ys = xs;          // ys points at the same array
ys[0] = 99;
System.out.println(xs[0]);   // 99
""", kicker="Value vs reference"),
    q("Why is <code>==</code> wrong for Strings?"),
    code("The trap", "java", r"""
String a = "hero";
String b = "hero";
System.out.println(a == b);        // true  -- both interned

String c = new String("hero");
System.out.println(a == c);        // false -- different objects
System.out.println(a.equals(c));   // true  -- same characters
""", caption="The first case is only true because of the string pool. Do not rely on it."),
    big("<code>==</code> compares identity. <code>equals</code> compares value.",
        "For every object you write, you decide what &ldquo;equal&rdquo; means."),
    bullets("The equals/hashCode contract", [
        "If <code>a.equals(b)</code> then <code>a.hashCode() == b.hashCode()</code>",
        "The converse is <em>not</em> required &mdash; collisions are legal",
        "Break this and your objects vanish inside a <code>HashSet</code>",
        "Override both, or neither. Never one.",
    ]),
    code("Records give you both for free", "java", r"""
public record Position(int x, int y) {
    public Position translate(int dx, int dy) {
        return new Position(x + dx, y + dy);
    }
}
// equals, hashCode, toString and accessors are generated
// and the object is immutable
""", caption="Use records for value objects. You will want <code>Position</code> in the project."),
    bullets("Collections you will actually use", [
        "<code>List&lt;T&gt;</code> &mdash; ordered, duplicates allowed (<code>ArrayList</code>)",
        "<code>Set&lt;T&gt;</code> &mdash; no duplicates (<code>HashSet</code>, <code>LinkedHashSet</code>)",
        "<code>Map&lt;K,V&gt;</code> &mdash; key to value (<code>HashMap</code>)",
        "<code>Deque&lt;T&gt;</code> &mdash; queue or stack (<code>ArrayDeque</code>)",
        "Program to the <em>interface</em>, construct the implementation",
    ]),
    code("Program to the interface", "java", r"""
List<Element> walls = new ArrayList<>();   // yes
ArrayList<Element> bad = new ArrayList<>(); // no

// swapping the implementation later costs one line, not fifty
""" ),
    q("Interface or abstract class?"),
    two("The rule of thumb", "interface", """
<ul><li>A capability: <code>Drawable</code>, <code>Movable</code></li>
<li>A class can implement many</li>
<li>No state</li>
<li>Your default choice</li></ul>""",
        "abstract class", """
<ul><li>A partial implementation to share</li>
<li>A class can extend only one</li>
<li>Can hold state</li>
<li>Use when there is real shared code</li></ul>"""),
    code("Both, together", "java", r"""
public interface Drawable {
    void draw(GUI gui);
    default boolean isVisible() { return true; }   // default method
}

public abstract class Element implements Drawable {
    private Position position;
    protected Element(Position position) { this.position = position; }
    public Position getPosition() { return position; }
}
"""),
    bullets("Exceptions", [
        "<strong>Checked</strong> &mdash; declared, caller must handle: <code>IOException</code>",
        "<strong>Unchecked</strong> &mdash; programming errors: <code>NullPointerException</code>, <code>IllegalArgumentException</code>",
        "Throw unchecked for &ldquo;the caller made a mistake&rdquo;",
        "Never <code>catch (Exception e) {}</code>. An empty catch block is a lie.",
    ]),
    code("try-with-resources", "java", r"""
try (Screen screen = terminalFactory.createScreen()) {
    screen.startScreen();
    gameLoop(screen);
}   // close() is called for you, even if gameLoop throws
"""),
    part("Part two", "The build"),
    q("Why not just press Run in IntelliJ?"),
    big("Because the build has to run without you.",
        "On a teammate's laptop. On a grading machine. On CI at 3am."),
    bullets("What a build system does", [
        "Compiles sources in the right order",
        "Fetches and pins dependencies",
        "Runs the tests",
        "Produces a runnable artefact",
        "Does all of it identically, every time, for everyone",
    ]),
    big("Repetitive, with variations.",
        "That is the definition of something a human should stop doing by hand."),
    bullets("The Gradle lifecycle", [
        "<code>compileJava</code> &rarr; <code>processResources</code> &rarr; <code>classes</code>",
        "<code>compileTestJava</code> &rarr; <code>test</code>",
        "<code>jar</code> &rarr; <code>assemble</code>",
        "<code>check</code> &rarr; <code>build</code>",
        "Tasks declare dependencies; Gradle works out the order and skips what is up to date",
    ], tight=True),
    code("build.gradle.kts", "kotlin", r"""
plugins {
    java
    application
}

java { toolchain { languageVersion = JavaLanguageVersion.of(21) } }

repositories { mavenCentral() }

dependencies {
    implementation("com.googlecode.lanterna:lanterna:3.1.2")
    testImplementation(platform("org.junit:junit-bom:5.10.2"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testImplementation("org.mockito:mockito-core:5.11.0")
}

application { mainClass = "com.ldts.game.Application" }

tasks.test { useJUnitPlatform() }
"""),
    code("The commands", "bash", r"""
./gradlew build      # compile + test + assemble
./gradlew test       # tests only
./gradlew run        # run the application
./gradlew tasks      # what else can I do?
./gradlew clean      # when you no longer trust anything
"""),
    q("Why <code>./gradlew</code> and never <code>gradle</code>?"),
    big("The wrapper pins the version.",
        "Your build works on my machine because it downloads <em>your</em> Gradle, not mine."),
    bullets("Dependencies", [
        "<code>implementation</code> &mdash; needed to compile and run",
        "<code>testImplementation</code> &mdash; needed only by tests",
        "Coordinates are <code>group:artifact:version</code>",
        "Pin exact versions. <code>latest.release</code> is how builds start failing on their own.",
        "Transitive dependencies are pulled in for you &mdash; and so are their conflicts",
    ]),
    q("Two libraries want different versions of the same dependency. Now what?"),
    bullets("Conflict resolution", [
        "Gradle picks the <em>highest</em> version by default",
        "<code>./gradlew dependencies</code> shows you the resolved graph",
        "You can force a version, or exclude a transitive one",
        "When something breaks mysteriously after adding a library, look here first",
    ]),
    lab("Lab 2", [
        "Create the project skeleton with the Gradle wrapper",
        "Add Lanterna, get a window on screen with <code>./gradlew run</code>",
        "Add JUnit 5 and make one trivial test pass",
        "Break a dependency version deliberately and read the failure",
    ]),
    takeaways([
        "Primitives are copied, objects are referenced",
        "<code>equals</code>/<code>hashCode</code> travel together; records give you both",
        "Program to the interface",
        "If it only builds in your IDE, it does not build",
    ]),
]

# ================================================================== WEEK 03

W03 = [
    part("Part one", "To err is human"),
    big("Software has bugs."),
    q("Why?"),
    big("Humans write software.",
        "Computers execute it exactly as written."),
    bullets("Three words people use interchangeably, and should not", [
        "<strong>Error</strong> &mdash; a human action that produces an incorrect result",
        "<strong>Fault</strong> &mdash; the incorrect code that action left behind (the &ldquo;bug&rdquo;)",
        "<strong>Failure</strong> &mdash; the observable wrong behaviour, when the fault is executed",
    ]),
    big("A fault only becomes a failure when it is reached.",
        "Most of testing is the art of reaching things."),
    q("Is it a bug, or is it a feature?"),
    two("Two different questions", "Verification", """
<p><strong>Did we build the product right?</strong></p>
<ul><li>Against the specification</li>
<li>Internal consistency</li>
<li>Tests, reviews, static analysis</li></ul>""",
        "Validation", """
<p><strong>Did we build the right product?</strong></p>
<ul><li>Against what the client needs</li>
<li>Requires talking to humans</li>
<li>Demos, acceptance testing</li></ul>"""),
    big("A program can be perfectly verified and completely useless.",
        "Both questions have to be asked."),
    q("Where does the mismatch come from?"),
    bullets("Specification vs need", [
        "The client knows the problem, not the solution",
        "The specification is a <em>translation</em>, and translations lose things",
        "Small, frequent transformations lose less than one big one",
        "This is the argument for iterating &mdash; not fashion",
    ]),
    part("Part two", "What can I test, and how"),
    q("What can be tested?"),
    big("Every development artefact.",
        "Requirements, designs, diagrams, documentation &mdash; not only source code."),
    q("How do I test?"),
    bullets("Three postures", [
        "<strong>As a mathematician</strong> &mdash; prove correctness against a specification",
        "<strong>As an accountant</strong> &mdash; inspect, guided by experience and standards",
        "<strong>As an engineer</strong> &mdash; run it enough times",
    ]),
    q("When is <em>enough</em>, enough?"),
    quote("Testing shows the presence, not the absence of bugs.",
          "Edsger W. Dijkstra"),
    big("Static and dynamic verification are complements.",
        "Reviews find what tests cannot reach. Tests find what reviewers read past."),
    part("Part three", "Automating it"),
    q("Suppose you test the game by playing it. What is wrong with that?"),
    bullets("Manual testing through the UI", [
        "Difficult to set up &mdash; how do you reach that exact state?",
        "Expensive to repeat &mdash; a human has to do it again, every time",
        "Not reproducible &mdash; did you press the same keys?",
        "Reports nothing &mdash; there is no record afterwards",
    ]),
    big("So we need a tool.",
        "One that stores the tests, runs them, and tells us what happened."),
    bullets("The deal a test framework offers", [
        "You write <em>what</em> to check",
        "It does the plumbing: discovery, setup, isolation, teardown, reporting",
        "For each test: set up context &rarr; run &rarr; assert &rarr; tear down",
        "In this course: <strong>JUnit 5</strong>",
    ]),
    code("Your first JUnit 5 test", "java", r"""
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

class PositionTest {

    @Test
    void translateMovesByDelta() {
        Position p = new Position(3, 4);

        Position moved = p.translate(1, -2);

        assertEquals(new Position(4, 2), moved);
    }
}
""", caption="Arrange &middot; Act &middot; Assert. Three blocks, in that order, always."),
    code("Lifecycle", "java", r"""
class BankTest {
    private Bank bank;

    @BeforeEach void setUp()     { bank = new Bank("International"); }
    @AfterEach  void tearDown()  { bank.close(); }

    @BeforeAll  static void once() { /* expensive, shared setup */ }

    @Test void newBankHasNoAccounts() {
        assertEquals(0, bank.accountCount());
    }
}
""", caption="<code>@BeforeEach</code> runs before <em>every</em> test. Each test gets a fresh object."),
    big("Every test starts from a known state.",
        "If test B only passes when test A ran first, you have two bugs."),
    code("Expecting failure", "java", r"""
@Test
void depositInWrongCurrencyIsRejected() {
    Account account = bank.open("PT50", Currency.EUR);

    assertThrows(IncorrectCurrencyException.class,
                 () -> account.deposit(Money.of(100, Currency.CHF)));
}
""", caption="Assert on the exception <em>type</em>, not on a boolean you set in a catch block."),
    bullets("Assertions worth knowing", [
        "<code>assertEquals</code>, <code>assertNotEquals</code>",
        "<code>assertTrue</code>, <code>assertFalse</code> &mdash; add a message, or failures are unreadable",
        "<code>assertThrows</code>",
        "<code>assertAll</code> &mdash; report several failures at once instead of stopping at the first",
        "<code>assertSame</code> &mdash; identity, not equality. Rare, and usually a mistake.",
    ]),
    code("Naming that survives", "java", r"""
// what happened?
@Test void test1() { ... }
@Test void testHero() { ... }

// what is guaranteed?
@Test void heroCannotWalkThroughWall() { ... }
@Test void emptyArenaHasNoElements() { ... }
""", caption="A failing test name should tell you what broke without opening the file."),
    bullets("Where the tests live", [
        "<code>src/main/java/com/ldts/game/Arena.java</code>",
        "<code>src/test/java/com/ldts/game/ArenaTest.java</code>",
        "Two trees, same package structure",
        "Test code is production code. It gets reviewed, and it gets refactored.",
    ], tight=True),
    lab("Lab 3", [
        "Wire JUnit 5 into the Gradle build",
        "Write tests for a supplied <code>Numbers</code> class, from its specification only",
        "Make each test fail first, then pass",
        "Find the two faults we planted",
    ]),
    takeaways([
        "Error &rarr; fault &rarr; failure: three different things",
        "Verification and validation answer different questions",
        "Arrange, Act, Assert &mdash; one behaviour per test",
        "A test that depends on another test is not a test",
    ]),
]

# ================================================================== WEEK 04

W04 = [
    part("Part one", "Before you run anything"),
    q("What is the cheapest defect to fix?"),
    big("The one found before the code runs."),
    bullets("Reviews and inspections", [
        "Applicable to <em>every</em> artefact, not just code",
        "Driven by a checklist of the errors that actually recur",
        "Fagan (1986): inspections detect over 60% of defects",
        "The checklist is the point &mdash; memory is not a process",
    ]),
    bullets("What automation does for free", [
        "Style: a formatter ends the argument permanently",
        "<code>Checkstyle</code>, <code>PMD</code>, <code>SpotBugs</code>, <code>Error Prone</code>",
        "The compiler warnings you have been ignoring",
        "Use them <em>while</em> coding, not the night before delivery",
    ]),
    part("Part two", "How much testing is enough"),
    q("When do you stop testing?"),
    bullets("Honest answers", [
        "When the defect discovery rate flattens out",
        "When seeded faults are being found &mdash; <em>fault injection</em>",
        "When the risk left is smaller than the cost of continuing",
        "When time runs out &mdash; the usual one, and the worst one",
    ]),
    big("Fault injection asks: how good is my test suite?",
        "Inject known faults, see how many the suite catches. Week 11 turns this into a tool."),
    part("Part three", "Two ways in"),
    two("Black box vs white box", "Black box", """
<p>Test against the <strong>specification</strong>.</p>
<ul><li>You see inputs and outputs</li>
<li>Survives reimplementation</li>
<li>Cannot know what it missed</li></ul>""",
        "White box", """
<p>Test against the <strong>implementation</strong>.</p>
<ul><li>You see the code</li>
<li>Can target every branch</li>
<li>Breaks when the code is refactored</li></ul>"""),
    code("The same operation, two views", "java", r"""
// Specification
//   pop(stack)
//   pre : stack is not empty
//   post: returns and removes the most recently pushed element
//
// Black box test values: empty stack, one element, many elements

// Implementation
//   stack is an ordered set with a top index
//
// White box test values: top == 0, top == capacity, top in between
"""),
    part("Part four", "White-box coverage"),
    q("Your tests pass. What fraction of the code did they even execute?"),
    svg("A control flow graph", CFG,
        caption="Coverage criteria are questions about paths through this graph."),
    bullets("Four criteria, increasing in strength", [
        "<strong>Statement</strong> &mdash; every statement executed at least once",
        "<strong>Branch</strong> &mdash; every decision taken both true and false",
        "<strong>Condition</strong> &mdash; every atomic condition takes both values",
        "<strong>Path</strong> &mdash; every independent path executed",
    ]),
    code("Where statement coverage lies to you", "java", r"""
int divide(int a, int b) {
    if (b != 0) {
        return a / b;
    }
    return 0;
}

// one test: divide(10, 2)
//   statement coverage: 3 of 4 lines  -> looks fine
//   branch coverage:    1 of 2        -> the b == 0 case is untested
""", caption="100% statement coverage does not imply 100% branch coverage."),
    q("<code>if (a &amp;&amp; b)</code>. Branch coverage needs two tests. Condition coverage needs how many?"),
    code("Decision vs condition", "java", r"""
if (a && b) { ... }

// Branch (decision) coverage:  (true,true) and (false,anything)
// Condition coverage:          a true and false; b true and false
// MC/DC:                       each condition shown to independently
//                              affect the outcome
""", caption="Java short-circuits <code>&amp;&amp;</code>: if <code>a</code> is false, <code>b</code> never evaluates."),
    bullets("Cyclomatic complexity", [
        "<em>V(G) = decisions + 1</em>",
        "The number of independent paths through a method",
        "Also: a lower bound on the tests you need for path coverage",
        "Also: a decent smell detector. <code>V(G) &gt; 10</code> in one method is a design problem, not a testing problem.",
    ]),
    code("JaCoCo in the build", "kotlin", r"""
plugins { jacoco }

tasks.test { finalizedBy(tasks.jacocoTestReport) }

tasks.jacocoTestReport {
    dependsOn(tasks.test)
    reports { html.required = true; xml.required = true }
}

tasks.jacocoTestCoverageVerification {
    violationRules {
        rule { limit { counter = "BRANCH"; minimum = "0.70".toBigDecimal() } }
    }
}
""", caption="<code>./gradlew test jacocoTestReport</code> &rarr; <code>build/reports/jacoco/test/html/index.html</code>"),
    big("Coverage is a <em>floor</em>, not a target.",
        "Low coverage proves you are not testing. High coverage proves nothing."),
    q("How do I get 100% coverage with a test suite that asserts nothing?"),
    code("Like this", "java", r"""
@Test
void coversEverything() {
    new Arena(10, 10).update();   // executes the code
}                                 // asserts nothing at all
""", caption="Green. 100%. Worthless. Week 11 is about detecting exactly this."),
    part("Part five", "Black-box coverage"),
    q("The method signature is <code>fine(long daysLate)</code>. How many inputs are there?"),
    big("2<sup>64</sup>.",
        "Are they all semantically different? Obviously not."),
    bullets("Equivalence partitioning", [
        "Split the input domain into non-overlapping sets",
        "Within a set, the program should behave the same way",
        "Test one value per set",
        "The sets come from the <em>specification</em>, not the code",
    ]),
    code("Partitioning a specification", "java", r"""
// spec: if (daysLate <= MAX_FINE_PERIOD) fine = daysLate * DAILY_FINE
//       else                             fine = MAX_FINE

// partitions for daysLate
//   [ ..., -1 ]                  invalid    -> what should happen?
//   [ 0 ]                         boundary
//   [ 1 .. MAX_FINE_PERIOD ]      linear fine
//   [ MAX_FINE_PERIOD+1 .. ]      capped fine
"""),
    q("Where do defects cluster?"),
    big("At the edges.",
        "Off-by-one is the most common bug in the profession."),
    bullets("Boundary value analysis", [
        "For each partition, test the value just inside each edge",
        "And the value just outside it",
        "And the edge itself",
        "For <code>0 &le; d &le; MAX</code>: <code>-1, 0, 1, MAX-1, MAX, MAX+1</code>",
    ]),
    table("Putting both together", ["Partition", "Representative", "Boundaries"], [
        ["invalid", "-20", "-1"],
        ["zero", "0", "0"],
        ["linear", "10", "1, MAX&minus;1"],
        ["capped", "MAX+50", "MAX, MAX+1"],
    ]),
    lab("Lab 4", [
        "Add JaCoCo; get a coverage report on last week's tests",
        "Find a method with 100% statement and &lt;60% branch coverage",
        "Derive test values for a supplied specification by partitioning and BVA",
        "Compute the cyclomatic complexity of the worst method in your code",
    ]),
    takeaways([
        "Reviews are cheaper than tests; tests are cheaper than users",
        "Statement coverage is the weakest criterion &mdash; report branch coverage",
        "Coverage measures execution, not verification",
        "Partition the input domain, then attack the edges",
    ]),
]
