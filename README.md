# Lost in Tokenization: Script Invariance Failures in COMET-based Neural MT Evaluation

> **Status:** Under review

---

## Abstract

COMET is widely used as the primary quality signal for non-English machine translation, but its implicit **Script Invariance** assumption — that adequacy is reflected regardless of which script encodes the target — is rarely tested. This work treats romanisation as a controlled causal intervention on the **IndicMT Eval** corpus (7,000 MQM-annotated sentences across five low-resource Indic languages): rewriting target text into Latin script preserves all linguistic content and isolates the effect of orthographic form.

Romanisation eliminates **93.3%** of between-language COMET variance, confirming script identity — not language family — as the dominant factor behind cross-language differences. The same intervention collapses COMET–human correlation by **29–62%** and inflates inference cost by up to **5.57×**. This is traced to an inversion between Tokenization Parity (TP) and Information Parity (IP): romanisation simultaneously inflates tokenisation overhead and reduces semantic density per token.

Three inference-time diagnostics are introduced:

- **SBI (Script Bias Index):** Expected encoder pieces spent per unit of information recovered. Flag ≥ 3.0 marks unreliable scores.
- **IPI (IP Parity Index):** Distance from English-equivalent parity, with three empirical reliability zones — Parity, Burden, Paradox.
- **Computational Tax (LP × EP):** The joint multiplicative overhead of romanisation; ranges from 1.75× (Gujarati) to 5.57× (Tamil).

These diagnostics quantify, zone-classify, and cost the failure without retraining, and are recommended for reporting alongside COMET for any non-Latin-script target.

---

## Key Findings

| Finding | Value |
|---|---|
| Script explains (ANOVA η²) | **22.9%** of native COMET variance |
| Romanisation reduces script variance | **93.3%** (η² → 1.5%) |
| COMET–human correlation loss under romanisation | **29–62%** across five languages |
| Computational Tax range | **1.75× (GUJ) → 5.57× (TAM)** |
| Entropy Penalty share of ln(Tax) | **62–75%** across languages |
| HIN–GUJ gap collapse under romanisation | **13.95 → 2.29 pts** (84% reduction) |
| All Indic languages (romanised) | Cross into **Paradox zone** (IPI ≥ 0.70) |

---

## Datasets

### Primary — IndicMT Eval (Indic Languages)

This project uses the **IndicMT Eval** MQM dataset, created by [AI4Bharat](https://github.com/AI4Bharat).

| Property | Details |
|---|---|
| **Languages** | Gujarati (GUJ), Hindi (HIN), Malayalam (MAL), Marathi (MAR), Tamil (TAM) |
| **Task** | English → Indic MT quality evaluation |
| **Annotation** | MQM across 11 error types, 3 severity levels |
| **Size** | 1,400 MQM-annotated sentences × 5 languages = 7,000 sentences |
| **Source** | [github.com/AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval) |
| **Paper** | Sai et al. (2023). IndicMT Eval: A Dataset to Meta-Evaluate MT Metrics for Indian Languages. ACL 2023. |

### Cross-Linguistic Controls — WMT24 (German & Spanish)

Latin-script controls are drawn from the **WMT24 General MT Shared Task**, accessed via Google Research's [mt-metrics-eval](https://github.com/google-research/mt-metrics-eval) toolkit.

| Property | Details |
|---|---|
| **Language pairs** | English → German (EN-DE), English → Spanish (EN-ES) |
| **EN-DE** | 6,006 rows · 18 MT systems · MQM annotations |
| **EN-ES** | 4,651 rows · 14 MT systems · MQM + ESA annotations |
| **Source** | [github.com/google-research/mt-metrics-eval](https://github.com/google-research/mt-metrics-eval) |
| **Paper** | Kocmi et al. (2024). Findings of the WMT24 General MT Shared Task. WMT 2024, pp. 1–46. ACL. |

---

## Repository Structure

```
script-bias-comet-indic-mt/
│
├── README.md                         ← This file
├── requirements.txt                  ← Python dependencies
├── LICENSE                           ← MIT License
│
├── data/
│   ├── indic/
│   │   ├── README.md                 ← Dataset credit & reproduction instructions
│   │   └── indic_mt_eval_metrics.xlsx← Processed Indic dataset with all metrics
│   └── latin/
│       ├── README.md                 ← Dataset credit & reproduction instructions
│       └── wmt24_ende_enes_metrics.xlsx ← Processed WMT24 dataset with all metrics
│
├── notebooks/
│   ├── indic/
│   │   ├── 01_fetch_indicmt_eval.ipynb
│   │   ├── 02_romanisation_pipeline.ipynb
│   │   ├── 03_metric_scoring.ipynb
│   │   ├── 04_tp_ip_sbi_ipi.ipynb
│   │   ├── 05_statistical_tests.ipynb
│   │   ├── 06_computational_tax.ipynb
│   │   ├── 07_extra_metrics.ipynb
│   │   ├── 08_sentence_length_analysis.ipynb
│   │   └── 09_metric_human_alignment.ipynb
│   └── latin/
│       ├── 01_reproduce_wmt24_core.ipynb
│       ├── 02_compute_sentence_metrics.ipynb
│       ├── 03_tp_ip_sbi_ipi_latin.ipynb
│       └── 04_extra_metrics_latin.ipynb
│
└── results/
    ├── figures/
    ├── tables/
    └── scores/
```

---

## Installation

> **Python 3.10 required.** The AI4Bharat transliteration library does not support 3.11+.

### Step 1 — Clone the repository

```bash
git clone https://github.com/John-salvin/script-bias-comet-indic-mt.git
cd script-bias-comet-indic-mt
```

### Step 2 — Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows
```

### Step 3 — Install dependencies

**CPU (any machine, no GPU required)**

```bash
pip install -r requirements.txt
```

All notebooks run correctly on CPU; scoring 7,000 sentences will be slower (plan for 30–60 min per metric).

**GPU (NVIDIA, recommended for `indic/03_metric_scoring`)**

Install the CUDA build of PyTorch matching your driver **before** running `pip install -r requirements.txt`:

```bash
# CUDA 12.1
pip install torch==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121

# CUDA 11.8
pip install torch==2.5.1+cu118 --index-url https://download.pytorch.org/whl/cu118

# Then install the rest
pip install -r requirements.txt
```

Not sure which CUDA version you have? Run `nvidia-smi` — the top-right corner shows the driver's CUDA version.

### Step 4 — Launch JupyterLab

```bash
jupyter lab
```

Open the notebooks in order starting from `notebooks/indic/01_fetch_indicmt_eval.ipynb`.

---

## Dependencies

See `requirements.txt` for the full pinned list. Key libraries:

- `unbabel-comet` — COMET and COMET-QE scoring
- `bert-score` — BERTScore
- `BLEURT` — BLEURT scoring
- `transformers` — XLM-RoBERTa tokenizer (TP / IP)
- `ai4bharat-transliteration`, `indic-transliteration` — Romanisation pipeline
- `sacrebleu` — chrF, BLEU, TER
- `scipy` — Statistical testing (Welch's t, ANOVA, Spearman ρ)
- `pandas`, `numpy` — Data processing
- `matplotlib`, `seaborn` — Visualisation

---

## Reproducing Results

Run the Indic notebooks in order from `notebooks/indic/01_fetch_indicmt_eval.ipynb`, then the Latin notebooks from `notebooks/latin/01_reproduce_wmt24_core.ipynb`.

| Finding | Notebook |
|---|---|
| Script explains 22.9% of COMET variance (ANOVA η²) | `indic/05_statistical_tests.ipynb` |
| Romanisation reduces variance by 93.3% | `indic/04_tp_ip_sbi_ipi.ipynb` |
| TP–IP Inversion across 5 languages | `indic/04_tp_ip_sbi_ipi.ipynb` |
| Computational Tax (1.75×–5.57× overhead) | `indic/06_computational_tax.ipynb` |
| COMET–human alignment collapse (29–62%) | `indic/09_metric_human_alignment.ipynb` |
| Latin-script controls (DEU Burden / SPA Parity) | `latin/03_tp_ip_sbi_ipi_latin.ipynb` |

---

## License

MIT License — see [LICENSE](LICENSE).

The **IndicMT Eval** dataset is governed by its own license from [AI4Bharat](https://github.com/AI4Bharat/IndicMT-Eval). The **WMT24** data is governed by the terms of the [mt-metrics-eval](https://github.com/google-research/mt-metrics-eval) repository.
