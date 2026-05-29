# Lesson: A Graph You Can Multiply

This first stage is small on purpose.

It has only two synthetic documents, ten sections, seven references, and eight findings. That is not enough to impress anyone with scale. It is enough to make the shape of the problem visible.

The point of a baseline stage is not to be clever. The point is to produce something that works, something that can be rerun, and something plain enough that every later improvement can be measured against it.

In this stage, the central idea is simple:

> Legal documents form dependency structures.

A statute section may cite another section. An internal policy may implement a statute. A claims workflow may rely on a form. A form may rely on a regulator's circular. A circular may have been superseded. A clause may point to something that no longer exists.

If we write those relationships down, we have a graph.

But if we arrange that graph carefully, we also have a matrix.

That is where the experiment starts to become interesting.

## The First Representation

The probe begins with plain Markdown. A heading like this:

```markdown
## Section 300. Minimum Coverage
```

creates a section node:

```text
section:300
```

And a sentence like this:

```text
An insurer shall provide minimum liability coverage as described in Section 310.
```

creates a directed edge:

```text
section:300 -> section:310
```

The arrow means:

```text
Section 300 depends on Section 310.
```

That direction matters. It is easy to get turned around here.

If Section 300 cites Section 310, then Section 300 is the dependent thing. Section 310 is the dependency. If Section 310 changes, Section 300 may need review.

This is the same shape as software:

```text
Policy.cs imports Rules.cs
Policy.cs depends on Rules.cs
```

In legal text:

```text
Section 300 cites Section 310
Section 300 depends on Section 310
```

Different domain. Same dependency shape.

## The Matrix

Once we have numbered the nodes, the graph can be written as a matrix.

The convention in this sandbox is:

```text
A[i, j] = 1 means node i depends on node j
```

Rows are the things doing the depending.

Columns are the things being depended on.

So if:

```text
section:300 -> section:310
```

then:

```text
A[section:300, section:310] = 1
```

That one little `1` says: "to understand 300, go look at 310."

Most of the matrix is zero. That is normal. Legal documents, like software systems, are usually sparse. Each section depends on a few other sections, not every other section.

The baseline emits this matrix as:

```text
output/adjacency_matrix.csv
```

This is the direct dependency matrix. It tells us only what is one step away.

## Two Steps Away

Now suppose Section 10 depends on Section 300, and Section 300 depends on Section 900.

In arrow form:

```text
section:10 -> section:300 -> missing:900
```

There is no direct arrow from Section 10 to Section 900. But Section 10 still relies on Section 900 indirectly.

This is where matrix multiplication becomes useful.

The matrix product:

```text
A^2
```

answers the question:

> What can I reach in exactly two dependency steps?

In this stage, `two_hop_matrix.csv` shows that Section 10 reaches `missing:900` in two hops:

```text
section:10 -> section:300 -> missing:900
```

That is a tiny result, but it is the seed of impact analysis.

If an internal manual implements a statute section, and that statute section cites something missing, expired, repealed, or superseded, then the internal manual may inherit the problem.

The debt is not local anymore.

It propagates.

## Transitive Closure

Two hops are useful, but real systems are rarely so polite.

A policy may cite a regulation that cites a statute that delegates authority to an agency that issues a bulletin that points to a form.

The general question is:

> What can this node reach through any number of dependency steps?

That is transitive closure.

The baseline writes this to:

```text
output/transitive_closure.csv
```

For each node, the closure matrix shows all reachable dependencies.

This gives us a different kind of legal tooling. Instead of asking a human to manually follow chains of cross-references, we can ask:

```text
What does this clause ultimately depend on?
```

or:

```text
Which internal policies are touched if this external authority changes?
```

That second question is one of the big product questions hiding inside this sandbox.

## Missing Nodes Are Still Nodes

One design choice in this stage is important:

> A missing reference is kept in the matrix.

If Section 300 references Section 900, but Section 900 does not exist in the corpus, the probe creates:

```text
missing:900
```

This might feel odd at first. Why create a node for something that does not exist?

Because the absence is the finding.

If we drop the missing node, the matrix becomes cleaner, but less truthful. The dependency disappeared from the data structure even though it is present in the document.

Keeping `missing:900` lets the matrix say:

```text
section:300 -> missing:900
section:10 -> missing:900
```

The first line is direct.

The second line is inherited through Section 300.

That is useful.

It means a dangling legal reference can have a blast radius.

## Roots

The sandbox also computes dependency roots.

In this stage, a dependency root is:

> A reachable dependency with no further reachable dependencies.

So Section 300 has roots:

```text
section:310
missing:900
```

Section 310 has no further dependencies. The missing Section 900 also has no further dependencies because there is no actual text to follow.

For Section 10, the roots are also:

```text
section:310
missing:900
```

Section 10 does not directly cite Section 900. But it depends on Section 300, and Section 300 cites Section 900. The root calculation makes that inherited dependency visible.

This is the beginning of a useful review question:

> Which terminal authorities does this internal artifact ultimately rest on?

In a real compliance system, some of those roots should be statutes, regulations, forms, circulars, court decisions, or internal control documents.

If a root is missing, stale, ambiguous, or unowned, the artifact that depends on it may be risky.

## Cycles

The sample corpus also includes a deliberate cycle:

```text
section:400 -> section:410
section:410 -> section:400
```

The closure matrix detects that both nodes can reach themselves through a dependency path.

That is why the output lists:

```text
section:400
section:410
```

as cycle nodes.

A cycle is not automatically wrong. Legal texts often have exceptions, definitions, and cross-references that loop in ways humans can still interpret.

But a cycle is a place to look carefully.

In software, cycles make systems harder to build, test, and modify.

In legal documents, cycles can make obligations harder to interpret, audit, and retire.

This is why a cycle detector belongs in the earliest version of the sandbox.

Not because every cycle is a defect.

Because every cycle is a question.

## The First False Positive

The first version of this stage made a useful mistake.

It treated section headings as references.

This heading:

```markdown
## Section 300. Minimum Coverage
```

was accidentally read as:

```text
section:300 -> section:300
```

That created a self-cycle for every section.

This is the sort of bug that looks silly after it is fixed, but it teaches something important:

> Legal parsing cannot be only text search.

The parser needs to know where it is in the document. A heading is not the same kind of text as a body sentence. A definition is not the same as an obligation. A citation in a footnote may not mean the same thing as a citation in a rule.

Even in the toy corpus, structure matters.

That lesson will come back again.

## What This Stage Proves

This stage proves only a few things, but they are enough.

It proves that:

- plain text can be turned into section nodes
- simple references can be turned into dependency edges
- edges can be represented as a matrix
- matrix multiplication can reveal indirect dependencies
- closure can reveal full reachability
- missing references can be preserved as explicit nodes
- cycles can be detected from the closure
- useful review evidence can be emitted as Markdown, JSON, and CSV

It does not prove that this approach will scale.

It does not prove that regex parsing is enough.

It does not prove that the legal interpretation is correct.

It does not prove that dense matrices are the right final data structure.

Those are later questions.

This stage has a humbler job:

> Establish a working baseline that can be cloned, criticized, and improved.

That is exactly what it does.

## The Lesson

A graph shows relationships.

A matrix lets us calculate with them.

For legal tech debt, that distinction matters. The graph is how humans see the structure. The matrix is how the machine can propagate it, square it, close it, compare it, and eventually optimize it.

The best early architecture may not be either graph or matrix.

It may be both:

- graph language for explanation
- matrix language for computation
- human review for legal meaning

That gives us a useful next direction.

Stage 001 is the baseline. It shows the idea working in miniature.

Stage 002 can ask the performance question:

> How fast can this become if we treat legal dependency analysis as a matrix problem?
