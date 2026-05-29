# Lesson: A Reference Is Not Yet a Relationship

This lesson belongs to `004-typed-edge-study`.

The Kentucky sample gave us a bigger graph, and the bigger graph taught us a quiet but important lesson: the word "reference" is too small.

In the first stages, every edge meant the same thing. Section A referenced Section B. That was enough to discover dangling references, simple cycles, dependency roots, and transitive closure. It was enough to build a dashboard. It was even enough to make the matrix visible.

But legal meaning does not live in the arrow alone.

An internal claims playbook that says it "implements" a statute is not doing the same thing as a statute that "defines" a term. A notice workflow that sends a file to a producer communication queue is not doing the same thing as a recordkeeping rule that says what evidence must be retained. A stale checklist that cites a missing section should not be treated as a valid path just because the string `Section 9999` appears in a sentence.

The graph can see all of these as arrows. A lawyer, compliance analyst, or product owner cannot.

## The Question

The question for this stage is:

Can we classify edges so that reachability means something closer to legal or compliance access?

Plain reachability asks whether one node can reach another through any path. Typed reachability asks whether it can reach another through a valid kind of path.

That difference is the whole stage.

## The Smallest Example

Consider two paths from the Kentucky sample.

The first path is simple:

`section:1000 -> section:304.39.010`

The source is an internal playbook scope section. The target is a synthetic statute-like purpose section. The sentence says the playbook implements that authority. This looks like an `implements_authority` edge.

The second path is different:

`section:1120 -> missing:9999`

The sentence says historical checklists still cite a missing section and must be retired. That is not a valid legal dependency. It is a `stale_reference` edge. It should be visible, but it should not behave like a live authority path.

Both are references. They should not produce the same kind of reachability.

## The Representation

This stage starts with a taxonomy.

The first proposed edge types include:

- `cites_authority`
- `implements_authority`
- `validates_against`
- `workflow_handoff`
- `requires_evidence`
- `records_retention`
- `notice_requirement`
- `proof_requirement`
- `reporting_requirement`
- `exception_process`
- `definition_dependency`
- `coordinates_with`
- `review_loop`
- `stale_reference`

In matrix terms, this suggests that one adjacency matrix is no longer enough.

Instead, we can think in layers:

- `A_implements`
- `A_cites`
- `A_workflow`
- `A_evidence`
- `A_stale`
- and so on

The question is then not only whether `A` reaches a target. It is whether a composed path through these typed matrices is allowed.

## What Worked

The Kentucky sample created enough variety to make typing necessary. If the graph had stayed small, typing would have felt like over-engineering.

Now it feels like the next natural step.

The dashboard already gives us the right review surface. We can click a cell, inspect a witness path, and ask what each edge in that path means. That is exactly where the typed-edge study should live.

## What Surprised Us

The surprising thing is that "cycle" became ambiguous.

In the toy corpus, a two-node cycle looked suspicious almost by definition. In the Kentucky sample, many cycles are just structural feedback between authority, procedure, evidence, and review. Some are defects. Some are ordinary governance.

This is not a small distinction. A detector that reports every cycle as a problem will train users to ignore it. A typed detector can be more careful. It can say, for example, that an `implements_authority` edge followed by a `cites_authority` edge is not the same thing as a workflow loop that reopens itself forever.

## What This Proves

This stage proves that the next bottleneck is semantic, not computational.

We can make matrices faster later. But a fast matrix over vague edges gives us vague answers at high speed.

The first thing to do is decide what the edges mean.

## What This Does Not Prove

This stage does not yet prove that our taxonomy is complete.

It does not prove that edge types can be extracted automatically.

It does not prove that a legal SME would agree with our labels.

It gives us a working study frame and a seed queue for finding out.

## The Next Question

The next question is implementation:

Can we turn the seed labels into typed matrices and compute typed witness paths that explain why a target is reachable, not merely that it is reachable?
