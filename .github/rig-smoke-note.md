# rig smoke fixture

This file lives under `.github/` on purpose: `FileClassificationHelper.IsCiFile`
returns true for any path starting with `.github/`, which should make
`BuildSystemAnalysisModule` add the `CI` label.
