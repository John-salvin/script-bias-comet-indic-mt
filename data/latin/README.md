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
| `German_Spanish_COMET_QE.xlsx` | Final processed dataset — COMET, COMET-QE, TP, IP, SBI, IPI, and derived metrics for EN-DE and EN-ES (two sheets: German, Spanish) |
| `reproduce_wmt24_core.py` | Standalone Python script to reproduce the raw WMT24 annotation data from scratch using `mt-metrics-eval` |

---

## How to Reproduce the Raw Data

The raw WMT24 human evaluation data is not committed to this repository. Use the provided script to reproduce it from the public source.

### Step 1 — Install dependencies

```bash
pip install mt-metrics-eval sacrebleu pandas openpyxl
```

### Step 2 — Download WMT data (~2 GB, run once)

```bash
python -c "from mt_metrics_eval import data; data.Download()"
```

This downloads the WMT evaluation data to `~/.mt-metrics-eval/`.

### Step 3 — Run the reproduce script

```bash
python reproduce_wmt24_core.py
```

This produces `wmt24_core_ende_enes.xlsx` with two sheets (German, Spanish) containing:

| Column | Description |
|---|---|
| `lang_pair` | `en-de` or `en-es` |
| `system` | MT system name (e.g. GPT-4, Gemini-1.5-Pro) |
| `domain` | `news` / `social` / `speech` / `literary` |
| `doc` | Document name from WMT24 |
| `seg_id` | 1-based segment index within the document |
| `source` | English source sentence |
| `target` | MT system output |
| `refA` | Human reference translation A |
| `rater` | Annotator ID (rater1 … rater10) |
| `category` | MQM error category (or `No-error`) |
| `severity` | `no-error` / `minor` / `major` / `critical` / `neutral` |
| `error_start` | Character offset of error span start (NaN if no error) |
| `error_end` | Character offset of error span end (NaN if no error) |
| `mqm_score` | −(avg of top-5 per-rater penalties); 0 = perfect, negative = errors |
| `esa_score` | ESA direct assessment 0–100 (EN-ES only; NaN if not rated) |

Once you have the raw data, continue with the notebooks in `notebooks/latin/`.
