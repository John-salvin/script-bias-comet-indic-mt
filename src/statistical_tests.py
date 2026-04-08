"""
Statistical Testing Suite
==========================
All 9 statistical tests used to validate script bias findings.

Author: G L John Salvin, IIT Palakkad (2026)
"""

import numpy as np
from scipy import stats
from statsmodels.stats.anova import AnovaRM
import pandas as pd


def run_all_tests(native_scores, romanized_scores, language_labels=None):
    """
    Run all 9 statistical tests on COMET scores for native vs. romanized text.

    Tests included:
    1. Paired t-test
    2. Wilcoxon signed-rank test
    3. Mann-Whitney U test
    4. Cohen's d (effect size)
    5. Eta-squared (variance explained)
    6. Levene's test (variance equality)
    7. Kolmogorov-Smirnov test (distribution equality)
    8. Pearson correlation
    9. Spearman rank correlation

    Args:
        native_scores (list[float]): COMET scores for native script.
        romanized_scores (list[float]): COMET scores for romanized text.
        language_labels (list[str], optional): Language label per sentence.

    Returns:
        dict: Results for all 9 tests.
    """
    native = np.array(native_scores)
    roman = np.array(romanized_scores)

    results = {}

    # 1. Paired t-test
    t_stat, p_ttest = stats.ttest_rel(native, roman)
    results["paired_ttest"] = {"t": t_stat, "p": p_ttest, "significant": p_ttest < 0.05}

    # 2. Wilcoxon signed-rank test
    w_stat, p_wilcoxon = stats.wilcoxon(native, roman)
    results["wilcoxon"] = {"W": w_stat, "p": p_wilcoxon, "significant": p_wilcoxon < 0.05}

    # 3. Mann-Whitney U test
    u_stat, p_mw = stats.mannwhitneyu(native, roman, alternative="two-sided")
    results["mann_whitney"] = {"U": u_stat, "p": p_mw, "significant": p_mw < 0.05}

    # 4. Cohen's d
    pooled_std = np.sqrt((native.std() ** 2 + roman.std() ** 2) / 2)
    d = (native.mean() - roman.mean()) / pooled_std if pooled_std > 0 else 0
    results["cohens_d"] = {"d": d, "interpretation": "large" if abs(d) > 0.8 else "medium" if abs(d) > 0.5 else "small"}

    # 5. Eta-squared
    all_scores = np.concatenate([native, roman])
    grand_mean = all_scores.mean()
    ss_between = len(native) * (native.mean() - grand_mean) ** 2 + len(roman) * (roman.mean() - grand_mean) ** 2
    ss_total = np.sum((all_scores - grand_mean) ** 2)
    eta_sq = ss_between / ss_total if ss_total > 0 else 0
    results["eta_squared"] = {"eta2": eta_sq, "variance_explained_pct": eta_sq * 100}

    # 6. Levene's test
    lev_stat, p_levene = stats.levene(native, roman)
    results["levene"] = {"W": lev_stat, "p": p_levene, "equal_variance": p_levene > 0.05}

    # 7. Kolmogorov-Smirnov test
    ks_stat, p_ks = stats.ks_2samp(native, roman)
    results["ks_test"] = {"KS": ks_stat, "p": p_ks, "same_distribution": p_ks > 0.05}

    # 8. Pearson correlation
    r_pearson, p_pearson = stats.pearsonr(native, roman)
    results["pearson"] = {"r": r_pearson, "p": p_pearson}

    # 9. Spearman rank correlation
    r_spearman, p_spearman = stats.spearmanr(native, roman)
    results["spearman"] = {"rho": r_spearman, "p": p_spearman}

    return results


def print_test_summary(results):
    """Print a formatted summary of all test results."""
    print("=" * 60)
    print("STATISTICAL TEST SUMMARY")
    print("=" * 60)
    for test_name, vals in results.items():
        print(f"\n{test_name.upper().replace('_', ' ')}")
        for k, v in vals.items():
            if isinstance(v, float):
                print(f"  {k}: {v:.4f}")
            else:
                print(f"  {k}: {v}")


if __name__ == "__main__":
    np.random.seed(42)
    native_comet = np.random.normal(0.75, 0.10, 500).tolist()
    roman_comet = np.random.normal(0.52, 0.12, 500).tolist()
    results = run_all_tests(native_comet, roman_comet)
    print_test_summary(results)
