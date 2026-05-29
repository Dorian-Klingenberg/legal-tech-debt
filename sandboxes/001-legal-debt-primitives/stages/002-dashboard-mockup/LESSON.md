# Lesson: Seeing a Dependency System

This lesson belongs to `002-dashboard-mockup`.

The first stage proved that a tiny legal corpus could be parsed into a few useful objects: sections, references, findings, roots, and cycles. That was enough to make the machinery work. It was not yet enough to make the machinery easy to think with.

That distinction matters. A program can produce correct JSON and still leave a human reader stranded. The next question is not merely "did the analysis run?" It is "can someone look at the result and understand where the legal debt is?"

This stage builds a dashboard mockup to start answering that question.

## The Question

We have a small dependency system. Section 10 points to Sections 300 and 310. Section 300 points to Section 310 and to a missing Section 900. Section 400 and Section 410 point to each other. A few definitions appear to be unused. A few references to outside authorities lack dates or versions.

The raw data is already meaningful, but it is scattered across several output files. A reviewer should not need to mentally join all of that on paper.

So the question for this stage is:

What interface makes the dependency system visible enough that we can reason about it?

There are really three smaller questions inside that one.

First, can we see direct relationships? That is the graph question. If a section points to another section, draw that arrow.

Second, can we see reachability? That is the matrix question. If a section can reach another section through one or more intermediate references, show that relationship as a calculated fact.

Third, can we see review work? That is the findings question. If something is dangling, circular, orphaned, or unversioned, present it as an item someone can inspect.

The dashboard is therefore not a final product. It is a laboratory bench. It lets us put the same specimen under three different lenses.

## The Smallest Example

The smallest useful example is not a large statute. It is this tiny synthetic corpus.

It contains ten sections:

- internal policy sections numbered 10, 20, 30, and 40
- state statute sections numbered 100, 200, 300, 310, 400, and 410
- one missing section, 900, referenced by Section 300 but not present in the corpus

That is small enough for a reader to hold in mind, but large enough to show several important failure modes.

Section 300 contains a dangling reference. It points to Section 900, and Section 900 does not exist in the extracted corpus. In a legal system, that might mean a repeal, a typo, a stale internal manual, or an omitted source document.

Section 400 and Section 410 form a cycle. Each one points to the other. Sometimes legal cross-references like this are legitimate. Sometimes they make interpretation harder. Either way, the system should expose the loop.

Section 200 defines terms that nothing else seems to use. That may be harmless. It may also be residue from an older policy model. The point is not to convict the definition automatically. The point is to place it in front of a reviewer.

This is why the toy corpus is useful. It is not pretending to be realistic in size. It is realistic in shape.

## The Representation

The dashboard uses four representations of the same underlying data.

The first representation is the section list. Each section has an id, a title, a kind, a source file, a line number, and body text. This is the human-readable layer. It tells us what the node means.

The second representation is the reference list. Each reference has a source section and a target section. This is the direct dependency layer. It tells us what points to what.

The third representation is the matrix. The rows are source nodes. The columns are target nodes. A filled cell means "the row node can reach the column node in this matrix view."

In direct adjacency mode, a filled cell means there is a direct reference.

In two-hop mode, a filled cell means the source can reach the target through exactly two reference steps.

In closure mode, a filled cell means the source can reach the target through any number of reference steps.

The fourth representation is the findings list. This is the review layer. It does not try to show every relationship. It shows the items that deserve attention.

None of these representations is enough by itself.

A graph is good for spatial recognition. A cycle can be seen as a little loop. A missing node can be colored differently. But graphs become crowded as systems grow.

A matrix is good for calculation. It can show reachability, closure, and eventually typed relationships. But matrices are abstract. The reader has to know what the row and column labels mean.

A findings list is good for work management. It tells a reviewer what to do next. But it can feel ungrounded unless the reviewer can jump back to the section and its dependencies.

The dashboard therefore keeps them together.

## What Worked

The first successful thing is simply that the data can be embedded into a single static HTML file.

That is not the architecture we would choose forever, but it is the right architecture for this stage. It removes all accidental complexity. There is no server to run, no database to migrate, no framework decision to defend, and no build system to nurse back to health.

The second successful thing is the drill-down panel. Clicking a node gives the reader a compact summary:

- what the section says
- what it points to
- what points to it
- whether it has terminal roots
- whether it participates in a cycle
- whether there are nearby findings

That panel is important because visualization without inspection becomes decoration. The graph can invite attention, but the drill-down has to answer the next question.

The third successful thing is the side-by-side existence of graph and matrix views. The graph gives an immediate picture. The matrix turns the same relationships into a form that can be multiplied, closed, filtered, and compared.

This is where the earlier matrix discussion starts to become concrete. A dependency graph can be traversed. A dependency matrix can be multiplied or otherwise combined. The dashboard lets us present both concepts without choosing prematurely between them.

The fourth successful thing is that the missing node is visible. `missing:900` appears as a node even though no section body exists for it. That is a small but important product decision. Missing references are not just errors in an output file. They are objects in the review world.

The fifth successful thing is that a matrix cell can now become a question.

When the reader clicks the cell for `section:10` and `section:300` in the direct adjacency matrix, the dashboard treats that cell as a claim: Section 10 directly depends on Section 300. The graph highlights the two nodes and the edge between them. The selected-node panel underneath the matrix shows the dependency orders for Section 10, including the fact that the highest order with new information is `A^2`.

This matters because a matrix by itself can feel mute. A `1` in a cell is correct, but it does not explain itself. A witness path gives the `1` a story. It says, in effect: here is the route through the dependency system that made this cell true.

## What Surprised Us

The main surprise is how quickly a tiny corpus begins to need multiple views.

With seven references, the graph is still readable. But even here, different questions want different shapes. A reviewer looking for a circular reference wants the graph. A reviewer looking for terminal dependencies wants closure. A reviewer triaging legal work wants the findings queue.

Another surprise is that the matrix view is not only a performance idea. It is also a user-interface idea.

At first, a dependency matrix sounds like an implementation detail. It is the sort of thing one might hide behind a function called `compute_closure`. But when it is shown as a table, it becomes a thinking surface. The reviewer can see that the row is a starting point, the column is a possible destination, and the cell is the answer to a reachability question.

This is helpful for learning. It turns a mathematical structure into something visible.

The awkward part is scale. A matrix with ten or twenty nodes is friendly. A matrix with ten thousand nodes is not. That does not make the matrix useless. It means the interface will need filtering, grouping, search, summarization, and probably several levels of abstraction.

The same is true for the graph. A graph of ten nodes can be drawn by hand. A graph of ten thousand nodes becomes a hairball unless it is clustered, filtered, or projected into task-specific slices.

So the stage teaches a useful caution: the core data structure and the human presentation are related, but they are not the same problem.

## What This Proves

This stage proves that the current extractor output is already sufficient to drive a meaningful reviewer interface.

It proves that the output objects have enough shape:

- sections can become nodes
- references can become edges
- missing targets can become synthetic nodes
- dependency roots can become section-level summaries
- cycle nodes can become warnings
- findings can become review tasks

It also proves that a static mockup is a good tool at this phase. We can explore interaction patterns before choosing a production stack.

Most importantly, it proves that the dependency matrix idea is not only feasible in the abstract. It can be made visible next to the graph and compared against it. Direct adjacency, two-hop reachability, and transitive closure can all be shown from the same embedded data.

## What This Does Not Prove

This stage does not prove that the dashboard will scale.

It does not prove that SVG is the right graph technology, that an HTML table is the right matrix technology, or that the current layout is the right product design.

It does not prove that the legal detectors are accurate enough for real legal work. The corpus is synthetic. The parser is deliberately simple. The findings are seeded examples.

It also does not prove that matrix operations will be faster than graph traversal for our eventual workload. That depends on graph size, sparsity, update frequency, typed-edge semantics, hardware, and the exact questions we ask. Matrix methods can be extraordinarily fast when the representation and operations fit the problem. They can also waste memory when the matrix is sparse and huge.

The honest conclusion is narrower and stronger:

The matrix approach is worth exploring because it gives us a second computational model for dependency analysis, and it can be presented to a human in a way that supports understanding.

## The Next Question

The next stage should make relationships typed.

Right now an edge simply means "references." Real legal dependency work needs more than that. A section may define a term, require an action, cite an authority, create an exception, delegate to a form, rely on evidence, or incorporate outside guidance.

Those edge types matter because reachability may depend on the path.

For example, a compliance obligation might be reachable through a chain of required-action edges, but not through a mere definitional edge. An external authority might be relevant only if the path includes a governing citation and not just a background note.

That leads to the next experiment:

Can we encode edge types in a matrix-like representation and compute typed reachability without losing explainability?

The answer is probably yes, but the details matter. We may need one matrix per relationship type. We may need a small algebra where multiplying two relationship types produces a third meaning, or produces no valid path at all. We may need to keep witness paths so the dashboard can explain why a node is reachable, not merely assert that it is.

That is a good next stage because it connects the mathematical experiment to the legal product problem. The computer can calculate reachability quickly. The lawyer still needs to know what kind of reachability it is.
