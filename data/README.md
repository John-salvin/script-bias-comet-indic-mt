# Data

This folder contains data used in the experiments.

## ⚠️ Dataset Credit & Attribution

This project uses the **IndicMT-Eval MQM Dataset** created by the [AI4Bharat](https://github.com/AI4Bharat) team.

- **Repository:** [github.com/AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval)
- **Dataset Viewer:** [Google Sheets](https://docs.google.com/spreadsheets/d/1HEwlBTLvN2NOXLxiBpIt_GVdHkjyvIo8DvQrncgto74/edit?usp=sharing)
- **Paper (ACL 2023):** *IndicMT Eval: A Dataset to Meta-Evaluate Machine Translation Metrics for Indian Languages*

### Please cite both papers when using this dataset:

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

## Structure

```
data/
├── raw/         ← Original, unmodified IndicMT-Eval MQM dataset files
└── processed/   ← Preprocessed files (romanized versions, merged splits)
```

## Dataset Details

| Property | Details |
|---|---|
| Languages | Gujarati, Hindi, Malayalam, Marathi, Tamil |
| MT Systems | 7 popular MT systems |
| Error Types | 11 MQM error categories |
| Annotations | Human MQM annotations by language experts |
| Sentences | ~5,889 |

## How to Prepare Data

1. Download the MQM dataset from: [AI4Bharat/IndicMT-Eval](https://github.com/AI4Bharat/IndicMT-Eval/tree/master/Dataset)
2. Or view it directly: [Google Sheets link](https://docs.google.com/spreadsheets/d/1HEwlBTLvN2NOXLxiBpIt_GVdHkjyvIo8DvQrncgto74/edit?usp=sharing)
3. Place raw files in `data/raw/`
4. Run the preprocessing script:
   ```bash
   python src/preprocess.py
   ```
   This will generate romanized versions in `data/processed/`

> **Note:** Raw data files are excluded from this repo via `.gitignore` due to file size. Please download directly from the source above.
