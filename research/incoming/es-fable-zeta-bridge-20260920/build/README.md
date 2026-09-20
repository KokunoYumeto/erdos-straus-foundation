# Reproducible cumulative PDF build copy

`FABLE_TO_ORIGINAL_CONDUCTOR_BUILD.tex` is derived from the byte-preserved file in `../upstream/` solely to produce the readable cumulative PDF.

The frozen source is not edited. The build copy makes one syntax repair at original line 1312 (`\{...\}` closes the displayed set correctly), adds `hypertexnames=false` to prevent duplicate PDF anchors caused by manually tagged equations, breaks several long displays and filenames across lines, and uses smaller bibliography text to avoid a one-line final page. These changes do not alter a mathematical formula or claim.

The authoritative source identity remains:

```text
upstream/FABLE_TO_ORIGINAL_CONDUCTOR.tex
SHA-256 bfb75ff468f35b71103ad2671e22f20fee0414df4a43d1dab5fc2d19aabbd1b6
```

The generated PDF and visual-QA receipt are in `../output/pdf/` and `../pdf_qa.json`.
