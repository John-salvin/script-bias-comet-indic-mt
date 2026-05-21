# Notebooks

Notebooks are split into two self-contained folders:

| Folder | Corpus | Purpose |
|---|---|---|
| [`indic/`](indic/) | IndicMT Eval (5 languages × 1,400 sentences) | All Indic-side experiments, diagnostics, and statistics |
| [`latin/`](latin/) | WMT24 ENG-DEU / ENG-SPA | Latin-script control experiments |

## Prerequisites

Install dependencies from `requirements.txt` at the **root of the repository** (`script-bias-comet-indic-mt/requirements.txt`):

```bash
# from the repo root
pip install -r requirements.txt

# or from inside the notebooks/ folder
pip install -r ../requirements.txt
```

Before running any Indic notebook, place the five per-language processed CSV files in `../data/processed/` (i.e., `script-bias-comet-indic-mt/data/processed/`). WMT24 data is fetched automatically by `latin/01_reproduce_wmt24_core.ipynb`.

## Execution order

Run `indic/` notebooks 01 → 12 in sequence, then `latin/` notebooks 01 → 05. Each notebook reads outputs from the previous one — do not skip steps.

See the README inside each subfolder for the full notebook list and descriptions.
