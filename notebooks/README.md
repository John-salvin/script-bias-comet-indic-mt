# Notebooks

Run these notebooks **in order** to reproduce all results from the paper.

| # | Notebook | Description |
|---|---|---|
| 1 | `01_tokenization_parity.ipynb` | Compute TP scores across 5 Indic languages |
| 2 | `02_information_parity.ipynb` | Compute IP scores using BLOOM-560m |
| 3 | `03_script_bias_index.ipynb` | Compute SBI and variance explained by script |
| 4 | `04_computational_tax.ipynb` | Compute Computational Tax per language |
| 5 | `05_statistical_testing.ipynb` | Run all 9 statistical tests |
| 6 | `06_reproduce_paper_results.ipynb` | End-to-end reproduction of all paper tables/figures |

## Requirements

Make sure you've installed all dependencies first:
```bash
pip install -r ../requirements.txt
```

## Notes
- Notebooks 1–4 can be run independently.
- Notebook 6 requires notebooks 1–5 to have been run first (or the processed data to exist in `data/processed/`).
- Notebook 2 requires a GPU for reasonable speed (or significant patience on CPU).
