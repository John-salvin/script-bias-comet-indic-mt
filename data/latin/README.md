# Latin-Script Data (WMT24)

This folder contains data for the two Latin-script language pairs used as cross-linguistic controls:
**German (EN-DE)** and **Spanish (EN-ES)**, sourced from the WMT24 General MT Shared Task.

---

## Dataset Credit & Attribution

The dataset is derived from the **WMT24 General MT Shared Task**, accessed via Google Research's publicly available [mt-metrics-eval-v2](https://github.com/google-research/mt-metrics-eval) toolkit.

| Property | Details |
|---|---|
| **Source repository** | [github.com/google-research/mt-metrics-eval](https://github.com/google-research/mt-metrics-eval) |
| **Paper** | Kocmi et al. (2024). Findings of the WMT24 General MT Shared Task. *Proceedings of WMT 2024*, pp. 1–46. ACL. |
| **ACL Anthology** | [aclanthology.org/2024.wmt-1.1](https://aclanthology.org/2024.wmt-1.1/) |

### Dataset Statistics

| Language pair | Rows | MT systems | Sentences | Raters | Annotations |
|---|---|---|---|---|---|
| English → German (EN-DE) | 6,006 | 18 | 339 | 10 | MQM |
| English → Spanish (EN-ES) | 4,651 | 14 | 339 | 4 | MQM + ESA |

---

## Files

| File | Description |
|---|---|
| `Wmt24_ende_enes_metrics.xlsx` | Final processed dataset — COMET, COMET-QE, TP, IP, SBI, IPI, and derived metrics for EN-DE and EN-ES (two sheets: German, Spanish) |

---

## How to Reproduce the Raw Data

The raw WMT24 human evaluation data is not committed to this repository. To reproduce it from scratch, run the notebook `notebooks/latin/01_reproduce_wmt24_core.ipynb`, which requires:

```bash
pip install mt-metrics-eval sacrebleu pandas openpyxl
python -c "from mt_metrics_eval import data; data.Download()"
```

The download step fetches ~2 GB of WMT evaluation data to `~/.mt-metrics-eval/`. Once complete, run all cells in the notebook. Continue with the remaining notebooks in `notebooks/latin/`.
