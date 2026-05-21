# Script Bias in Neural MT Evaluation Metrics (COMET & Indic Languages)

> **Status:** Under review

---

## Abstract

This work exposes a fundamental script-conditioned bias in neural MT evaluation metrics — primarily COMET and BLEURT — when applied to Indic languages. Using the IndicMT Eval dataset (5,889 sentences across 5 languages and 11 error types), we show that script alone explains **22.9% of variance** in COMET scores. We introduce three novel metrics:

- **TP (Tokenization Parity):** Measures representational fairness at the tokenizer level
- **IP (Information Parity):** Measures semantic information preservation across scripts
- **SBI (Script Bias Index):** A unified measure of script-conditioned metric bias
- **Computational Tax:** The irrecoverable overhead (Length Penalty × Entropy Penalty) incurred by LLMs when processing romanised Indic text vs. native scripts

Romanization reduces script-driven variance by **93.3%** but degrades human alignment by **32–62%**, revealing the Tokenization–Information Paradox.

---

## Repository Structure

```
script-bias-comet-indic-mt/
│
├── README.md                    ← This file
├── requirements.txt             ← Python dependencies
├── LICENSE                      ← MIT License
│
├── data/
│   ├── README.md                ← How to obtain the IndicMT Eval dataset
│   ├── raw/                     ← Original dataset files (not committed — see data/README.md)
│   └── processed/               ← Preprocessed / romanised files
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
├── results/
│   ├── figures/
│   ├── tables/
│   └── scores/
│
└── paper/
    └── README.md                ← Citation information
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

All notebooks run correctly on CPU; scoring ~7,000 sentences will be slower (plan for 30–60 min per metric).

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
jupyterlab
```

Open the notebooks in order starting from `notebooks/indic/01_fetch_indicmt_eval.ipynb`.

---

## Dependencies

See `requirements.txt` for the full pinned list. Key libraries:

- `unbabel-comet` — COMET scoring
- `bert-score` — BERTScore
- `BLEURT` — BLEURT scoring
- `transformers` — XLM-RoBERTa tokenizer (TP/IP)
- `ai4bharat-transliteration`, `indic-transliteration` — Romanisation
- `sacrebleu` — chrF, BLEU, TER
- `scipy` — Statistical testing
- `pandas`, `numpy` — Data processing
- `matplotlib`, `seaborn` — Visualisation

---

## Dataset

This project uses the **IndicMT Eval** MQM dataset, created by [AI4Bharat](https://github.com/AI4Bharat).

| Property | Details |
|---|---|
| **Languages** | Gujarati, Hindi, Malayalam, Marathi, Tamil |
| **Task** | English → Indic MT quality evaluation |
| **Annotation** | MQM (Multidimensional Quality Metrics) |
| **Size** | ~5,889 sentences with human quality annotations |
| **Source** | [github.com/AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval) |

---

## Reproducing Results

Run the notebooks in order starting from `notebooks/indic/01_fetch_indicmt_eval.ipynb`.

| Finding | Notebook |
|---|---|
| Script explains 22.9% of COMET variance | `05_statistical_tests.ipynb` |
| Romanization reduces variance by 93.3% | `04_tp_ip_sbi_ipi.ipynb` |
| Computational Tax (1.75×–5.57× overhead) | `06_computational_tax.ipynb` |
| TP–IP Paradox across 5 languages | `04_tp_ip_sbi_ipi.ipynb` |

---

## License

MIT License — see [LICENSE](LICENSE).  
The IndicMT-Eval dataset is governed by its own license from [AI4Bharat](https://github.com/AI4Bharat/IndicMT-Eval).
