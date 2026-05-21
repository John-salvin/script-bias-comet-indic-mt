# Indic Notebooks

These twelve notebooks reproduce every Indic-side result in the paper, running on IndicMT Eval (Sai et al., 2023) — 1,400 MQM-annotated English→Indic sentence pairs per language (GUJ, HIN, MAL, MAR, TAM).

Run in order: each notebook writes outputs that the next one reads.

| # | Notebook | What it does |
|---|---|---|
| 01 | `01_fetch_indicmt_eval.ipynb` | Downloads and preprocesses the IndicMT Eval dataset; produces one CSV per language in `../data/processed/` |
| 02 | `02_romanisation_pipeline.ipynb` | Applies IndicXlit (Madhani et al., 2023) to all five target columns; adds romanised variants to each CSV |
| 03 | `03_metric_scoring.ipynb` | Runs COMET, BLEURT, BERTScore, BLEU, chrF, and TER on native and romanised conditions |
| 04 | `04_tokenization_parity.ipynb` | Computes Tokenization Parity (TP = Indic token count / English token count) using XLM-RoBERTa |
| 05 | `05_information_parity.ipynb` | Computes Information Parity (IP = NLL_English / NLL_Indic) using BLOOM-560M |
| 06 | `06_sbi_ipi_diagnostics.ipynb` | Derives SBI (= TP/IP) and IPI (= \|IP − 1\|) per sentence; assigns Parity / Burden / Paradox zones |
| 07 | `07_extra_metrics.ipynb` | Computes MATTR (w = 500), Byte Premium, and isolated dependent-vowel token counts (DV/1k) |
| 08 | `08_statistical_analysis.ipynb` | One-way ANOVA (η² native vs romanised), Welch's t-test for the HIN–GUJ natural experiment, Cohen's d |
| 09 | `09_metric_human_alignment.ipynb` | Sentence-level Spearman ρ between each metric and MQM scores, native and romanised |
| 10 | `10_sbi_zone_analysis.ipynb` | Sentence-level SBI ≥ 3.0 exceedance rates; IPI zone transition plot (Figure 2) |
| 11 | `11_severity_analysis.ipynb` | MAR severity inversion — mean ΔCOMET by MQM error bucket; group Spearman ρ |
| 12 | `12_computational_tax.ipynb` | Computational Tax decomposition: LP, EP, Tax = LP × EP, EP% of ln(Tax) |

## Key outputs

- `../data/processed/` — per-language CSVs with all metric scores and diagnostic columns
- `../data/processed/tokenization_outputs/` — XLM-R token counts and TP ratios
- `../outputs/` — summary CSVs and figures referenced in the paper

## References

- Sai et al. (2023). *IndicMT Eval.* ACL 2023. https://aclanthology.org/2023.acl-long.795
- Madhani et al. (2023). *Aksharantar.* EMNLP Findings 2023.
- Conneau et al. (2020). *XLM-RoBERTa.* ACL 2020.
- Rei et al. (2020). *COMET.* EMNLP 2020.
- Petrov et al. (2023). *Tokenizer unfairness.* NeurIPS 2023.
- Tsvetkov & Kipnis (2024). *Information Parity.* EMNLP Findings 2024.
