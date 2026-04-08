"""
Script Bias Index (SBI)
========================
A unified measure of script-conditioned bias in MT evaluation metrics.
SBI quantifies how much a metric's score is driven by script choice
rather than actual translation quality.

Author: G L John Salvin, IIT Palakkad (2026)
"""

import numpy as np
from scipy import stats


def compute_sbi(native_scores, romanized_scores):
    """
    Compute the Script Bias Index (SBI).

    SBI = (mean_native - mean_roman) / pooled_std

    A high absolute SBI means the metric is heavily biased by script choice.

    Args:
        native_scores (list[float]): Metric scores for native-script hypotheses.
        romanized_scores (list[float]): Metric scores for romanized hypotheses.

    Returns:
        dict: SBI value, effect size (Cohen's d), and statistical test results.
    """
    native = np.array(native_scores)
    roman = np.array(romanized_scores)

    # Effect size (Cohen's d)
    pooled_std = np.sqrt((native.std() ** 2 + roman.std() ** 2) / 2)
    cohens_d = (native.mean() - roman.mean()) / pooled_std if pooled_std > 0 else 0

    # Paired t-test
    t_stat, p_value = stats.ttest_rel(native, roman)

    # Variance explained by script (eta squared)
    all_scores = np.concatenate([native, roman])
    grand_mean = all_scores.mean()
    ss_between = len(native) * (native.mean() - grand_mean) ** 2 + \
                 len(roman) * (roman.mean() - grand_mean) ** 2
    ss_total = np.sum((all_scores - grand_mean) ** 2)
    eta_squared = ss_between / ss_total if ss_total > 0 else 0

    return {
        "sbi": float(cohens_d),
        "cohens_d": float(cohens_d),
        "eta_squared": float(eta_squared),
        "variance_explained_pct": float(eta_squared * 100),
        "mean_native": float(native.mean()),
        "mean_romanized": float(roman.mean()),
        "t_statistic": float(t_stat),
        "p_value": float(p_value),
        "significant": p_value < 0.05,
    }


if __name__ == "__main__":
    # Example: simulate COMET scores
    np.random.seed(42)
    native_comet = np.random.normal(0.75, 0.10, 100)
    roman_comet = np.random.normal(0.52, 0.12, 100)
    result = compute_sbi(native_comet.tolist(), roman_comet.tolist())
    print(f"SBI (Cohen's d): {result['sbi']:.4f}")
    print(f"Variance explained by script: {result['variance_explained_pct']:.1f}%")
    print(f"p-value: {result['p_value']:.2e}")
