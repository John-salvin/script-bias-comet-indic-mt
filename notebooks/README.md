# Notebooks

This folder contains Jupyter notebooks for reproducing the experiments and results from the paper.

## Notebooks

| Notebook | Description |
|---|---|
| `Romanization_Pipeline_v2.ipynb` | Romanization pipeline for all 5 Indic language scripts |
| `01_tokenization_parity.ipynb` | Computing Tokenization Parity (TP) using the XLM-RoBERTa tokenizer |
| `02_information_parity.ipynb` | Computing Information Parity (IP) using BLOOM-560M negative log-likelihood |

## How to Run

```bash
pip install -r ../requirements.txt
jupyter notebook
```

Run notebooks in the following order for full reproducibility:

1. `Romanization_Pipeline_v2.ipynb` — generates romanized variants of all language files
2. `01_tokenization_parity.ipynb` — tokenizes all files and computes TP ratios
3. `02_information_parity.ipynb` — reads tokenized CSVs from step 2 and computes IP scores
