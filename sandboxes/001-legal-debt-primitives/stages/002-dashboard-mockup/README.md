# Stage 002: Dashboard Mockup

This stage turns the first legal debt demo run into a static HTML dashboard/data drill-down mockup.

Run the probe from this folder:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

Then open [dashboard.html](dashboard.html) in a browser.

The mockup embeds the demo data directly in the HTML for now. That keeps the experiment small: no server, no build step, no framework, and no decision yet about the eventual visualization library.

The current interaction pass includes dark mode, selected-node dependency-order matrices, and clickable matrix cells that highlight witness paths back in the graph.

## What To Look At

- [dashboard.html](dashboard.html): graph, matrix, findings, and drill-down UI
- [STAGE.md](STAGE.md): experiment record and result
- [LESSON.md](LESSON.md): narrative lesson for this stage
- [MATRIX_NOTES.md](MATRIX_NOTES.md): notes on matrix dependency analysis
- [OBSERVATIONS.md](OBSERVATIONS.md): running observations from the sandbox
