# Journal: 2026-05-13 Work Session

Local workspace timestamp during setup: Wednesday, May 13, 2026, Eastern time.

Today started with a small but important question: whether the legal dependency graph should remain a graph, or whether the matrix representation was worth taking seriously.

The first answer was yes. The matrix is not just feasible; it is a useful way to think. A graph tells us what points to what, but a matrix lets us ask reachability questions in a compact, computable form. Multiplying the matrix, or computing closure, lets us see not only direct dependencies but dependency chains.

That opened the door to the staged sandbox structure.

We created the first preserved sandbox stage so that each experiment can stand on the previous one without destroying it. Stage 001 became the baseline. It held the original small corpus, the lightweight extractor, and the first lesson explaining what the prototype did and did not prove.

Stage 002 turned the extractor output into a dashboard. At first the dashboard was deliberately static: the data lived inside the HTML file. That was the right move. No server, no database, no framework. Just the question: can the output become something a person can inspect?

The answer was yes again. The dashboard gave us three views of the same dependency system:

- a graph for local visual structure
- a matrix for reachability
- a findings table for review work

Then the dashboard became interactive. Dark mode was added because this is going to be stared at for long stretches. Matrix cells became clickable. A selected cell began to act like a question: does this source reach this target? The dashboard learned to show a witness path and highlight the corresponding graph nodes and edges.

That was the first moment where the matrix stopped feeling abstract. A `1` in a cell was no longer just a symbol. It had a path behind it.

Stage 003 made the corpus larger and more realistic.

We created a synthetic Kentucky insurance sample, borrowing structure from Kentucky-style insurance statutes, proof-of-insurance regulation, and internal insurance workflows. The sample remained synthetic on purpose. We wanted realistic dependency behavior without pretending to give legal advice.

The new sample produced 60 sections, 197 references, 65 matrix nodes, and 48 findings.

That changed the character of the problem.

The graph was no longer a little teaching diagram. It became a navigation surface. Fixed node coordinates no longer made sense, so the dashboard moved to data-driven graph lanes grouped by document. The matrix became more important because it remained precise even as the graph became busy.

But the biggest lesson was not about scale. It was about meaning.

The Kentucky sample produced many cycles. Some were intentionally stale or suspicious. Some were ordinary feedback between a procedure and the authority it implements. Some were workflow loops where a claim file can be reopened. Some were evidence-retention relationships. A plain circular-reference detector could see the loop, but it could not say what kind of loop it was.

That realization changed the next stage.

The performance lab is still interesting, but it is no longer the next most important question. Making matrix multiplication faster would only give us faster answers over vague edges. The stronger next move is semantic: classify the edges.

So Stage 004 was created as the typed-edge study.

The working sentence for the day is:

A reference is not yet a relationship.

That sentence captures the turn. A section reference is evidence that one piece of text points to another. It does not tell us whether the source cites authority, implements authority, validates against a rule, hands work to another workflow, preserves evidence, creates a recordkeeping duty, invokes an exception, or points to a stale source that should be excluded from live reachability.

The new framework defines the first vocabulary for those distinctions. It starts with edge types such as `implements_authority`, `validates_against`, `workflow_handoff`, `requires_evidence`, `records_retention`, `notice_requirement`, `proof_requirement`, `reporting_requirement`, `exception_process`, `review_loop`, and `stale_reference`.

The stage also now has a seed labeling queue. It does not try to label everything yet. It chooses representative edges from the Kentucky sample so we can learn from concrete cases. That is important. If we design the taxonomy only in the abstract, it will probably be too neat. The snippets will keep us honest.

The next work should be patient:

1. Label the seed edges.
2. Notice where the taxonomy breaks.
3. Decide which edge types participate in live typed reachability.
4. Build one matrix per edge type.
5. Compare plain closure with typed closure.
6. Update the dashboard so witness paths explain relationship types, not just node sequences.

Today was a good day for the project because the work found its next real question.

We did not just make the prototype bigger. We discovered that bigger made it more honest.

The graph can show structure. The matrix can compute reachability. But the legal debt model needs meaning in the edges.
