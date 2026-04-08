"""
Computational Tax
=================
Quantifies the irrecoverable computational overhead incurred by LLMs
when processing romanised Indic languages vs. native scripts.

Computational Tax = Length Penalty (LP) × Entropy Penalty (EP)

Author: G L John Salvin, IIT Palakkad (2026)
"""

import numpy as np
from transformers import AutoTokenizer


def compute_length_penalty(native_texts, romanized_texts, tokenizer_name="xlm-roberta-base"):
    """
    Length Penalty (LP): Extra tokens required for romanized text.
    LP = romanized_token_count / native_token_count
    """
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    lp_scores = []
    for native, roman in zip(native_texts, romanized_texts):
        n_tok = len(tokenizer.encode(native, add_special_tokens=False))
        r_tok = len(tokenizer.encode(roman, add_special_tokens=False))
        lp = r_tok / n_tok if n_tok > 0 else None
        lp_scores.append(lp)
    return lp_scores


def compute_entropy_penalty(native_perplexities, romanized_perplexities):
    """
    Entropy Penalty (EP): Reduced meaning-per-token in romanized text.
    EP = romanized_perplexity / native_perplexity
    """
    ep_scores = []
    for n_ppl, r_ppl in zip(native_perplexities, romanized_perplexities):
        ep = r_ppl / n_ppl if n_ppl > 0 else None
        ep_scores.append(ep)
    return ep_scores


def compute_computational_tax(length_penalties, entropy_penalties):
    """
    Computational Tax = LP × EP

    A value of 2.0 means processing romanized text costs 2× as much
    compute as native script for the same semantic content.

    Args:
        length_penalties (list[float]): Per-sentence LP scores.
        entropy_penalties (list[float]): Per-sentence EP scores.

    Returns:
        dict: Per-sentence and aggregate Computational Tax scores.
    """
    taxes = []
    for lp, ep in zip(length_penalties, entropy_penalties):
        if lp is not None and ep is not None:
            taxes.append(lp * ep)
        else:
            taxes.append(None)

    valid = [t for t in taxes if t is not None]
    return {
        "per_sentence": taxes,
        "mean_tax": float(np.mean(valid)),
        "max_tax": float(np.max(valid)),
        "min_tax": float(np.min(valid)),
        "std_tax": float(np.std(valid)),
    }


# Example values from the paper
PAPER_RESULTS = {
    "Tamil":    {"lp": 2.31, "ep": 2.41, "tax": 5.57},
    "Malayalam": {"lp": 2.10, "ep": 2.01, "tax": 4.22},
    "Gujarati": {"lp": 1.65, "ep": 1.60, "tax": 2.64},
    "Marathi":  {"lp": 1.58, "ep": 1.58, "tax": 2.50},
    "Hindi":    {"lp": 1.40, "ep": 1.25, "tax": 1.75},
}

if __name__ == "__main__":
    print("Computational Tax Results from Paper:")
    print(f"{'Language':<12} {'LP':>6} {'EP':>6} {'Tax':>6}")
    print("-" * 34)
    for lang, vals in PAPER_RESULTS.items():
        print(f"{lang:<12} {vals['lp']:>6.2f} {vals['ep']:>6.2f} {vals['tax']:>6.2f}")
