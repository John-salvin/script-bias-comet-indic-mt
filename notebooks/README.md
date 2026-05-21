# Notebooks

Reproducibility notebooks for *Lost in Transliteration: Orthographic Sensitivity in Neural MT Evaluation*.

Notebooks are split into two self-contained folders:

| Folder | Corpus | Purpose |
|---|---|---|
| [`indic/`](indic/) | IndicMT Eval (5 languages × 1,400 sentences) | All Indic-side experiments, diagnostics, and statistics |
| [`latin/`](latin/) | WMT24 ENG-DEU / ENG-SPA | Latin-script control experiments |

## Prerequisites

```bash
pip install -r ../requirements.txt
```

Place the five per-language processed CSV files in `../data/processed/` before running any Indic notebook. WMT24 data is fetched automatically in `latin/01`.

## Execution order

Run `indic/` notebooks 01 → 12 in sequence, then `latin/` notebooks 01 → 05. Each notebook reads outputs from the previous one — do not skip steps.

See the README inside each subfolder for the full notebook list and descriptions.
