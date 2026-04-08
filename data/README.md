# Data

This folder contains data used in the experiments.

## Structure

```
data/
├── raw/         ← Original, unmodified IndicMT-Eval MQM dataset files
└── processed/   ← Preprocessed files (romanized versions, merged splits)
```

## Dataset Source

We use the **IndicMT-Eval** dataset:
- Paper: [IndicMT Eval: A Dataset to Meta-Evaluate Machine Translation Metrics for Indian Languages](https://aclanthology.org/2023.acl-long.795/)
- Download: https://github.com/AI4Bharat/IndicMT-Eval

## How to Prepare Data

1. Download the MQM dataset from the link above
2. Place raw files in `data/raw/`
3. Run the preprocessing script:
   ```bash
   python src/preprocess.py
   ```
   This will generate romanized versions in `data/processed/`

> **Note:** Raw data files are excluded from this repo via `.gitignore` due to size.
