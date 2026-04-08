# Notebooks

This folder contains Jupyter notebooks for reproducing the experiments and results from the paper.

## Notebooks

| Notebook | Description |
|---|---|
| `01_data_exploration.ipynb` | Initial exploration of the IndicMT-Eval MQM dataset |
| `02_romanization.ipynb` | Romanization pipeline for Indic language scripts |
| `03_metric_scores.ipynb` | Computing COMET, chrF, and BERTScore on native vs. romanized text |
| `04_script_bias_index.ipynb` | Computing the Script Bias Index (SBI), TP, and IP metrics |
| `05_statistical_tests.ipynb` | All 9 statistical tests (Wilcoxon, Friedman, etc.) |
| `06_figures.ipynb` | Generating all figures and tables from the paper |

## How to Run

```bash
pip install -r ../requirements.txt
jupyter notebook
```

Run notebooks in order (01 → 06) for full reproducibility.
