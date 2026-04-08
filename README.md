# Script Bias in Neural MT Metrics (COMET & Indic Languages)

> **Paper:** *Connecting the Dots: Script Bias in Neural MT Metrics*  
> **Author:** G L John Salvin, IIT Palakkad (2026)  
> **Status:** Under submission

---

## 📄 Abstract

This work exposes a fundamental script-conditioned bias in neural MT evaluation metrics — primarily COMET and BLEURT — when applied to Indic languages. Using the IndicMT Eval dataset (5,889 sentences across 5 languages and 11 error types), we show that script alone explains **22.9% of variance** in COMET scores. We introduce three novel metrics:

- **TP (Tokenization Parity):** Measures representational fairness at the tokenizer level
- **IP (Information Parity):** Measures semantic information preservation across scripts
- **SBI (Script Bias Index):** A unified measure of script-conditioned metric bias
- **Computational Tax:** The irrecoverable overhead (Length Penalty × Entropy Penalty) incurred by LLMs when processing romanised Indic text vs. native scripts

Romanization reduces script-driven variance by **93.3%** but degrades human alignment by **32–62%**, revealing the Tokenization–Information Paradox.

---

## 🗂️ Repository Structure

```
script-bias-comet-indic-mt/
│
├── README.md                  ← This file
├── requirements.txt           ← Python dependencies
├── LICENSE                    ← MIT License
│
├── data/
│   ├── README.md              ← How to download/access the IndicMT Eval dataset
│   └── sample/                ← Small sample data for quick testing
│
├── notebooks/
│   ├── 01_tokenization_parity.ipynb       ← TP computation
│   ├── 02_information_parity.ipynb        ← IP computation
│   ├── 03_script_bias_index.ipynb         ← SBI computation
│   ├── 04_computational_tax.ipynb         ← Computational Tax analysis
│   ├── 05_statistical_testing.ipynb       ← All 9 statistical tests
│   └── 06_reproduce_paper_results.ipynb   ← End-to-end reproduction notebook
│
├── src/
│   ├── __init__.py
│   ├── tokenization_parity.py     ← TP metric implementation
│   ├── information_parity.py      ← IP metric implementation
│   ├── script_bias_index.py       ← SBI metric implementation
│   ├── computational_tax.py       ← Computational Tax implementation
│   ├── romanization.py            ← Romanization pipeline for Indic languages
│   ├── comet_scoring.py           ← COMET/COMET-QE scoring utilities
│   └── statistical_tests.py       ← All statistical testing functions
│
├── results/
│   ├── figures/                   ← All paper figures (PNG/PDF)
│   └── tables/                    ← All paper tables (CSV)
│
└── paper/
    └── README.md                  ← Link to paper / citation info
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/John-salvin/script-bias-comet-indic-mt.git
cd script-bias-comet-indic-mt

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📦 Dependencies

See `requirements.txt` for the full list. Key libraries:

- `unbabel-comet` — COMET and COMET-QE scoring
- `transformers` — XLM-RoBERTa tokenizer (for TP/IP)
- `indic-nlp-library` — Indic language processing
- `scipy`, `statsmodels` — Statistical testing
- `pandas`, `numpy` — Data processing
- `matplotlib`, `seaborn` — Visualization

---

## 📊 Dataset

This project uses the **IndicMT Eval** dataset:
- 5 Indic languages: **Gujarati, Hindi, Malayalam, Marathi, Tamil**
- 11 MT error types
- ~5,889 sentences with human quality annotations

> **Download:** See `data/README.md` for instructions on accessing the IndicMT Eval dataset from its original source.

---

## 🔁 Reproducing Paper Results

To reproduce the main findings from the paper, run the notebooks **in order**:

```bash
# Launch Jupyter
jupyter notebook notebooks/
```

Or run the end-to-end script:

```bash
python src/run_all_experiments.py
```

### Key Results to Reproduce

| Finding | Notebook | Script |
|---|---|---|
| Script explains 22.9% of COMET variance | `05_statistical_testing.ipynb` | `statistical_tests.py` |
| Romanization reduces variance by 93.3% | `03_script_bias_index.ipynb` | `script_bias_index.py` |
| Computational Tax (1.75×–5.57× overhead) | `04_computational_tax.ipynb` | `computational_tax.py` |
| TP–IP Paradox across 5 languages | `02_information_parity.ipynb` | `information_parity.py` |
| COMET-QE DA drops (755% Hindi, 56% Tamil) | `05_statistical_testing.ipynb` | `comet_scoring.py` |

---

## 📐 Novel Metrics Defined

### Tokenization Parity (TP)
Measures whether a tokenizer allocates a proportional number of tokens to native-script vs. romanised text relative to semantic content.

### Information Parity (IP)
Measures how much semantic information (bits per token) is preserved when switching between scripts, using BLOOM-560M perplexity as a proxy.

### Script Bias Index (SBI)
A unified index: `SBI = f(TP, IP)` — quantifies how much a metric's score is driven by script choice rather than translation quality.

### Computational Tax
`Computational Tax = Length Penalty × Entropy Penalty`  
Quantifies the irrecoverable compute overhead for LLMs processing romanised Indic text vs. native scripts.

---

## 📋 Citation

If you use this code or build on this work, please cite:

```bibtex
@article{johnsalvin2026scriptbias,
  title   = {Connecting the Dots: Script Bias in Neural MT Metrics},
  author  = {G L John Salvin},
  year    = {2026},
  institution = {IIT Palakkad},
  note    = {Preprint}
}
```

---

## 🔗 Related Work & References

- **COMET:** Rei et al. (2020) — [Unbabel/COMET](https://github.com/Unbabel/COMET)
- **IndicMT Eval:** Panda et al. (2023) — [Dataset Paper](https://aclanthology.org/)
- **XLM-RoBERTa:** Conneau et al. (2020)
- **BLOOM:** BigScience Workshop (2022)
- **Indic NLP Library:** Kunchukuttan (2020)

---

## 📬 Contact

**G L John Salvin**  
Department of Computer Science and Engineering  
IIT Palakkad, Kerala, India  
GitHub: [@John-salvin](https://github.com/John-salvin)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
