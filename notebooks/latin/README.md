# Latin-Script Control Notebooks

These five notebooks reproduce the Latin-script control experiments in the paper, using WMT24 ENG-DEU and ENG-SPA MQM data (Kocmi et al., 2024) — 6,006 rows for ENG-DEU and 4,651 rows for ENG-SPA, pooled across MT systems.

The controls serve two roles: (1) anchor ENG-SPA in the Parity zone (IPI = 0.009) as a near-ideal reference, and (2) show via ENG-DEU that tokeniser fragmentation is architecture-driven, not script-surface — DEU uses the Latin alphabet yet exhibits IP suppression matching the Indic native-script range.

Run in order.

| # | Notebook | What it does |
|---|---|---|
| 01 | `01_reproduce_wmt24_core.ipynb` | Fetches WMT24 ENG-DEU and ENG-SPA from `mt-metrics-eval`; produces per-system sentence-level CSVs |
| 02 | `02_compute_sentence_metrics.ipynb` | Runs COMET, BLEURT, BERTScore, BLEU, chrF, and TER on both language pairs |
| 03 | `03_tp_ip_sbi_ipi_latin.ipynb` | Computes TP, IP, SBI, and IPI for DEU and SPA; places each language in its IPI zone |
| 04 | `04_extra_metrics_latin.ipynb` | Computes MATTR (w = 500), Byte Premium, single-token word-type fraction (1-tok%), and IP–COMET Pearson r |
| 05 | `05_deu_sbi_severity.ipynb` | SBI Reversal analysis: per-severity SBI for DEU (Kruskal–Wallis H = 135.0); contrasts the Indic direction |

## Key outputs

- `../data/latin/` — per-language-pair CSVs with all metric and diagnostic columns
- `../outputs/latin/` — summary tables referenced in the paper (Table 11, Table 12, Appendix G)

## References

- Kocmi et al. (2024). *Findings of WMT24.* WMT 2024. https://aclanthology.org/2024.wmt-1.1
- Conneau et al. (2020). *XLM-RoBERTa.* ACL 2020.
- Petrov et al. (2023). *Tokenizer unfairness.* NeurIPS 2023.
- Tsvetkov & Kipnis (2024). *Information Parity.* EMNLP Findings 2024.
- Arnett & Bergen (2025). *Byte Premium.* COLING 2025.
- Covington & McFall (2010). *MATTR.* Journal of Quantitative Linguistics.
