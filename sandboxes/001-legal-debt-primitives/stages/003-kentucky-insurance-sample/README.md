# Stage 003: Kentucky Insurance Sample

This stage replaces the tiny dashboard corpus with a larger synthetic Kentucky auto-insurance dependency sample.

Run the probe from this folder:

```powershell
python .\src\legal_debt_probe.py --corpus .\data\corpus --out .\output
```

After regenerating output, refresh the embedded dashboard data from the sandbox root:

```powershell
python .\tools\embed_dashboard_data.py .\stages\003-kentucky-insurance-sample
```

Then open [dashboard.html](dashboard.html) in a browser.

## What Changed

- 5 Markdown corpus files with Kentucky-style insurance/code/regulation/internal-control sample content
- 60 extracted sections
- 197 extracted references
- 65 matrix nodes
- dashboard graph layout is now data-driven instead of hand-positioned
- embedded dashboard data now comes from generated probe output

## Important Caveat

The corpus is synthetic sample data. It borrows Kentucky insurance subject matter and section-number shapes, but it is not legal authority and should not be used for legal interpretation.

See [SOURCE_NOTES.md](SOURCE_NOTES.md) for the official sources used only as structural inspiration.

## What To Look At

- [dashboard.html](dashboard.html): graph, matrix, findings, and drill-down UI
- [data/corpus](data/corpus): synthetic Kentucky-style corpus
- [output/report.md](output/report.md): generated report
- [SOURCE_NOTES.md](SOURCE_NOTES.md): source/inspiration notes
- [STAGE.md](STAGE.md): experiment record and result
- [LESSON.md](LESSON.md): narrative lesson for this stage
