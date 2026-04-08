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
├── CITATION.cff               ← Machine-readable citation
│
├── data/
│   ├── README.md              ← How to download/access the IndicMT Eval dataset
│   ├── raw/                   ← Original dataset files (not committed — see data/README.md)
│   └── processed/             ← Preprocessed/romanized files
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
│   ├── tables/                    ← All paper tables (CSV)
│   └── scores/                    ← Raw metric scores
│
└── paper/
    └── README.md                  ← Citation info
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

## 📊 Dataset & Credits

This project uses the **IndicMT Eval** MQM dataset, created by [AI4Bharat](https://github.com/AI4Bharat).

| Property | Details |
|---|---|
| **Languages** | Gujarati, Hindi, Malayalam, Marathi, Tamil |
| **Task** | English → Indic MT quality evaluation |
| **Annotation** | MQM (Multidimensional Quality Metrics) by human experts |
| **MT Systems** | 7 popular MT systems evaluated |
| **Error Types** | 11 MQM error categories |
| **Size** | ~5,889 sentences with human quality annotations |
| **Source** | [github.com/AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval) |
| **Dataset View** | [Google Sheets](https://docs.google.com/spreadsheets/d/1HEwlBTLvN2NOXLxiBpIt_GVdHkjyvIo8DvQrncgto74/edit?usp=sharing) |

### Indic-COMET Model Checkpoints (from AI4Bharat)

The IndicMT-Eval repository also provides fine-tuned COMET checkpoints for Indic languages:

| Model | Download |
|---|---|
| `indic-comet-mqm` | [Download checkpoint](https://objectstore.e2enetworks.net/indic-asr-public/data/anushka/comet_mqm_1.5e-5/comet_mqm_1.5e-5/checkpoints/epoch=2-step=1875-val_kendall=0.455.ckpt) |
| `indic-comet-da` | [Download checkpoint](https://objectstore.e2enetworks.net/indic-asr-public/data/anushka/comet_da_1.5e-5/comet_da_1.5e-5/checkpoints/epoch=3-step=2500-val_kendall=0.456.ckpt) |
| `hparams.yaml (DA)` | [Download](https://objectstore.e2enetworks.net/indic-asr-public/data/anushka/comet_da_1.5e-5/comet_da_1.5e-5/hparams.yaml) |
| `hparams.yaml (MQM)` | [Download](https://objectstore.e2enetworks.net/indic-asr-public/data/anushka/comet_mqm_1.5e-5/comet_mqm_1.5e-5/hparams.yaml) |

> **Please cite the IndicMT-Eval papers below if you use this dataset in your work.**

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

### Cite This Work

If you use this code or build on this work, please cite:

```bibtex
@article{johnsalvin2026scriptbias,
  title       = {Connecting the Dots: Script Bias in Neural MT Metrics},
  author      = {G L John Salvin},
  year        = {2026},
  institution = {IIT Palakkad},
  note        = {Preprint}
}
```

### Cite the IndicMT-Eval Dataset

If you use the IndicMT-Eval MQM dataset, **please also cite both of the following papers** from the AI4Bharat team:

```bibtex
@article{DBLP:journals/corr/abs-2212-10180,
  author    = {Ananya B. Sai and
               Tanay Dixit and
               Vignesh Nagarajan and
               Anoop Kunchukuttan and
               Pratyush Kumar and
               Mitesh M. Khapra and
               Raj Dabre},
  title     = {IndicMT Eval: {A} Dataset to Meta-Evaluate Machine Translation metrics
               for Indian Languages},
  journal   = {CoRR},
  volume    = {abs/2212.10180},
  year      = {2022},
  url       = {https://arxiv.org/abs/2212.10180}
}
```

```bibtex
@article{singh2024good,
  title   = {How Good is Zero-Shot MT Evaluation for Low Resource Indian Languages?},
  author  = {Singh, Anushka and Sai, Ananya B and Dabre, Raj and Puduppully, Ratish
             and Kunchukuttan, Anoop and Khapra, Mitesh M},
  journal = {arXiv preprint arXiv:2406.03893},
  year    = {2024}
}
```

---

## 🔗 References & Related Work

| Tool / Resource | Reference | Link |
|---|---|---|
| **IndicMT-Eval Dataset** | Sai et al. (2022), Singh et al. (2024) | [GitHub](https://github.com/AI4Bharat/IndicMT-Eval) |
| **COMET** | Rei et al. (2020) | [GitHub](https://github.com/Unbabel/COMET) |
| **XLM-RoBERTa** | Conneau et al. (2020) | [Paper](https://arxiv.org/abs/1911.02116) |
| **BLOOM** | BigScience Workshop (2022) | [HuggingFace](https://huggingface.co/bigscience/bloom-560m) |
| **Indic NLP Library** | Kunchukuttan (2020) | [GitHub](https://github.com/anoopkunchukuttan/indic_nlp_library) |
| **BERTScore** | Zhang et al. (2020) | [GitHub](https://github.com/Tiiiger/bert_score) |
| **chrF / chrF++** | Popović (2015, 2017) | [Paper](https://aclanthology.org/W15-3049/) |
| **NLG-Eval** (BLEU, METEOR, etc.) | Sharma et al. (2017) | [GitHub](https://github.com/Maluuba/nlg-eval) |
| **GenerationEval** (chrF++, TER, BLEURT) | Castro Ferreira et al. (2020) | [GitHub](https://github.com/WebNLG/GenerationEval) |
| **SummEval** (SMS, WMDo, MoverScore) | Fabbri et al. (2020) | [GitHub](https://github.com/Yale-LILY/SummEval) |

---

## 📬 Contact

**G L John Salvin**  
Department of Data Science  
IIT Palakkad, Kerala, India  
GitHub: [@John-salvin](https://github.com/John-salvin)

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.  
Note: The IndicMT-Eval dataset is governed by its own license from [AI4Bharat](https://github.com/AI4Bharat/IndicMT-Eval).
