# Indic Data

This folder contains data for the five Indic language pairs used in the experiments:
**Gujarati, Hindi, Malayalam, Marathi, Tamil** (English → Indic, MQM-annotated).

---

## Dataset Credit & Attribution

This project uses the **IndicMT-Eval MQM Dataset** created by the [AI4Bharat](https://github.com/AI4Bharat) team.

| Property | Details |
|---|---|
| **Repository** | [github.com/AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval) |
| **Dataset viewer** | [Google Sheets](https://docs.google.com/spreadsheets/d/1HEwlBTLvN2NOXLxiBpIt_GVdHkjyvIo8DvQrncgto74/edit?usp=sharing) |
| **Paper** | IndicMT Eval: A Dataset to Meta-Evaluate Machine Translation Metrics for Indian Languages (ACL 2023) |
| **Languages** | Gujarati, Hindi, Malayalam, Marathi, Tamil |
| **MT systems** | 7 popular MT systems |
| **Error types** | 11 MQM error categories |
| **Annotations** | Human MQM annotations by language experts |
| **Sentences** | ~5,889 |

Please cite both papers when using this dataset:

```bibtex
@article{DBLP:journals/corr/abs-2212-10180,
  author    = {Ananya B. Sai and Tanay Dixit and Vignesh Nagarajan and
               Anoop Kunchukuttan and Pratyush Kumar and
               Mitesh M. Khapra and Raj Dabre},
  title     = {IndicMT Eval: {A} Dataset to Meta-Evaluate Machine Translation
               metrics for Indian Languages},
  journal   = {CoRR},
  volume    = {abs/2212.10180},
  year      = {2022},
  url       = {https://arxiv.org/abs/2212.10180}
}

@article{singh2024good,
  title   = {How Good is Zero-Shot MT Evaluation for Low Resource Indian Languages?},
  author  = {Singh, Anushka and Sai, Ananya B and Dabre, Raj and Puduppully, Ratish
             and Kunchukuttan, Anoop and Khapra, Mitesh M},
  journal = {arXiv preprint arXiv:2406.03893},
  year    = {2024}
}
```

---

## Files

| File | Description |
|---|---|
| `indic_mt_eval_metrics.xlsx` | Final processed dataset — TP, IP, SBI, IPI, COMET, BLEURT, and all derived metrics for all 5 languages across native and romanised conditions |

---

## Folder Structure

```
data/indic/
└── indic_mt_eval_metrics.xlsx   ← Final processed dataset
```

---

## How to Get the Raw Data

The raw MQM annotation files are not included in this repository. Download them directly from [AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval/tree/master/Dataset) or view the dataset via the [Google Sheets link](https://docs.google.com/spreadsheets/d/1HEwlBTLvN2NOXLxiBpIt_GVdHkjyvIo8DvQrncgto74/edit?usp=sharing), then run the notebooks in order starting from `notebooks/indic/01_fetch_indicmt_eval.ipynb`.
