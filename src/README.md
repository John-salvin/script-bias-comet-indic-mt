# Source Code

This folder contains the core Python scripts used in the paper.

## Scripts

| File | Description |
|---|---|
| `preprocess.py` | Loads raw IndicMT-Eval data and prepares it for experiments |
| `romanize.py` | Romanization pipeline using `indic-transliteration` |
| `compute_metrics.py` | Computes COMET, chrF, BERTScore for native and romanized text |
| `script_bias_index.py` | Implements SBI (Script Bias Index), TP (Total Penalty), IP (Indic Penalty) |
| `statistical_tests.py` | Runs the 9 statistical significance tests from the paper |
| `utils.py` | Shared helper functions |

## Usage

See individual notebooks in `../notebooks/` for step-by-step usage of each module.
