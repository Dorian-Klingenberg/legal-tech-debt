# Lesson: When the Toy Corpus Grows Up

This lesson belongs to `003-kentucky-insurance-sample`.

The first corpus was small enough to understand in one glance. That was useful. A small example lets us see whether the machinery works at all.

But a legal dependency system does not stay small for long. A single insurance workflow can touch statutes, regulations, forms, notices, claims procedures, product controls, producer communications, recordkeeping, and external model guidance. The problem stops being "can we draw the graph?" and becomes "can we still reason when the graph has become a system?"

This stage makes that jump.

## The Question

The question is simple:

Can the same extractor, matrix outputs, and dashboard handle a more realistic legal/compliance dependency surface?

The new sample is still synthetic. That is deliberate. At this stage we want control. We want to seed missing references, reciprocal dependencies, orphan definitions, and unversioned authority references without pretending that we are interpreting real Kentucky law.

The corpus uses Kentucky-style auto-insurance subject matter because it is naturally tangled. Motor vehicle reparations, proof of insurance, PIP/no-fault workflows, cancellation and nonrenewal notices, adverse action records, and internal claims playbooks all point at one another.

## The Smallest Example

The smallest example in this stage is no longer two sections pointing at each other.

It is one internal workflow pointing into multiple authority layers.

For example, Section 1000 of the synthetic claims playbook references motor vehicle reparations, proof of insurance, cancellation notice, and a proof-of-insurance regulation. That one internal procedure immediately creates a dependency path across several documents.

That is closer to the real problem. A compliance failure rarely lives in one document. It appears in the space between documents.

## The Representation

The corpus is represented as Markdown files with numbered section headings. The extractor turns those files into:

- sections
- references
- findings
- matrix nodes
- direct adjacency matrix
- two-hop matrix
- transitive closure matrix
- dependency roots
- cycle nodes

The dashboard then embeds that output directly in HTML.

One important change was required: the graph layout could no longer be hand-positioned. The tiny corpus had explicit coordinates for every node. The Kentucky sample has 65 matrix nodes. Hand placement became brittle immediately.

So the dashboard now groups graph nodes into document lanes. That is a humble layout algorithm, but it is a meaningful step. It says the visualization must adapt to the corpus, not the other way around.

## What Worked

The extractor scaled from 10 sections and 7 references to 60 sections and 197 references without changing the core parsing logic.

That is encouraging. The parser is still primitive, but the data pipeline held together:

- Markdown in
- JSON/CSV/report out
- dashboard embedded from generated output
- graph, matrix, findings, and drill-down all still usable

The matrix became more interesting with the larger corpus. In the toy sample, the matrix was mostly a teaching device. Here it begins to feel necessary. The graph is useful for local context, but the matrix is better for asking precise questions: does this source reach that target, and at what order does the relationship first appear?

The witness-path interaction also becomes more valuable. A matrix cell says "reachable." The witness path says "here is why."

## What Surprised Us

The big surprise is the number of circular-reference findings.

Some are exactly the kind of thing we wanted to seed. Internal Section 1300 points to Section 1400, and Section 1400 points back to Section 1300. That is an easy cycle to understand.

But the larger sample also produces cycles that are structurally true and not necessarily bad. A statute-like section may point to an operational playbook, and the playbook may point back to the statute-like section it implements. A plain "circular reference" detector cannot distinguish a suspicious loop from a normal authority/implementation relationship.

This is not a failure of the detector. It is a lesson about the detector's meaning.

Plain edges are too blunt.

## What This Proves

This stage proves that the current sandbox can carry a larger fixture:

- 60 sections
- 197 references
- 65 matrix nodes
- 48 findings

It also proves that the static dashboard remains useful with a nontrivial corpus, provided the layout is generated from the data.

Most importantly, it proves that the next conceptual step is typed relationships. The larger sample does not merely make the graph bigger. It makes the semantics more important.

## What This Does Not Prove

This stage does not prove legal correctness.

The corpus is synthetic. It is inspired by Kentucky insurance structures, but the text is invented for experimentation. The dashboard is not a legal research tool.

This stage also does not prove that regex extraction will work on real statutes, regulations, policy forms, bulletins, PDFs, or internal manuals. Real documents will have inconsistent numbering, citations, tables, footnotes, amendments, cross-references, and nested subsections.

And it does not prove that the graph visualization will scale to thousands of nodes. It only proves that the dashboard survived the first meaningful jump in complexity.

## The Next Question

The next question is typed reachability.

Right now every edge means "references." That is not enough. A legal system needs to know whether a relationship means:

- cites authority
- implements authority
- defines term
- creates exception
- requires evidence
- delegates to procedure
- retains record
- supersedes or invalidates

Once edges have types, the matrix can become more than reachability. It can become typed reachability: not just "can A reach B?" but "can A reach B through a valid legal/compliance path?"

That is the real prize hiding under this stage.
