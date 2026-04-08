# Data

## IndicMT Eval Dataset

This project uses the **IndicMT Eval** dataset. Due to licensing, the full dataset is **not included** in this repository.

### How to Download

1. Visit the original IndicMT Eval dataset repository or paper:
   - Paper: [IndicMT Eval: A Dataset to Meta-Evaluate Machine Translation Metrics for Indian Languages](https://aclanthology.org/2023.acl-long.638/)
   - Dataset: Available on request from the authors or via HuggingFace Datasets

2. Place the downloaded files in `data/raw/`

### Expected Structure

```
data/
├── raw/
│   ├── indicmt_eval_gujarati.csv
│   ├── indicmt_eval_hindi.csv
│   ├── indicmt_eval_malayalam.csv
│   ├── indicmt_eval_marathi.csv
│   └── indicmt_eval_tamil.csv
├── processed/
│   ├── native_script/      ← Original script data
│   └── romanized/          ← Romanized versions
└── sample/
    └── sample_50.csv       ← 50-row sample for quick testing
```

### Languages Covered

| Language | Script | ISO Code |
|---|---|---|
| Gujarati | ગુજરાતી | gu |
| Hindi | हिन्दी | hi |
| Malayalam | മലയാളം | ml |
| Marathi | मराठी | mr |
| Tamil | தமிழ் | ta |
