"""
Tokenization Parity (TP) Metric
================================
Measures whether a tokenizer allocates a proportional number of tokens
to native-script vs. romanised Indic text relative to semantic content.

Author: G L John Salvin, IIT Palakkad (2026)
"""

from transformers import AutoTokenizer
import numpy as np


def compute_tokenization_parity(native_texts, romanized_texts, model_name="xlm-roberta-base"):
    """
    Compute Tokenization Parity (TP) between native-script and romanized text.

    Args:
        native_texts (list[str]): List of sentences in native script.
        romanized_texts (list[str]): Corresponding romanized sentences.
        model_name (str): HuggingFace tokenizer model name.

    Returns:
        dict: TP scores per sentence and aggregate statistics.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    tp_scores = []
    for native, roman in zip(native_texts, romanized_texts):
        native_tokens = len(tokenizer.encode(native, add_special_tokens=False))
        roman_tokens = len(tokenizer.encode(roman, add_special_tokens=False))

        # TP = ratio of native tokens to romanized tokens
        # TP < 1 means romanized uses more tokens (tokenizer disadvantages native)
        tp = native_tokens / roman_tokens if roman_tokens > 0 else None
        tp_scores.append({
            "native_text": native,
            "romanized_text": roman,
            "native_token_count": native_tokens,
            "romanized_token_count": roman_tokens,
            "tp_score": tp
        })

    scores = [s["tp_score"] for s in tp_scores if s["tp_score"] is not None]
    return {
        "per_sentence": tp_scores,
        "mean_tp": float(np.mean(scores)),
        "std_tp": float(np.std(scores)),
        "min_tp": float(np.min(scores)),
        "max_tp": float(np.max(scores)),
    }


if __name__ == "__main__":
    # Quick test
    native = ["நான் வீட்டிற்கு செல்கிறேன்"]
    roman = ["Naan veettiRku selgiRen"]
    result = compute_tokenization_parity(native, roman)
    print(f"Mean TP: {result['mean_tp']:.4f}")
