"""
Information Parity (IP) Metric
================================
Measures semantic information preservation (bits per token) when switching
between native and romanised Indic scripts, using language model perplexity.

Author: G L John Salvin, IIT Palakkad (2026)
"""

import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def compute_perplexity(texts, model, tokenizer, device="cpu"):
    """Compute per-token perplexity for a list of texts."""
    perplexities = []
    model.eval()
    with torch.no_grad():
        for text in texts:
            inputs = tokenizer(text, return_tensors="pt").to(device)
            loss = model(**inputs, labels=inputs["input_ids"]).loss
            perplexities.append(torch.exp(loss).item())
    return perplexities


def compute_information_parity(native_texts, romanized_texts, model_name="bigscience/bloom-560m"):
    """
    Compute Information Parity (IP) between native-script and romanized text.

    IP measures how much semantic information (bits per token) is preserved
    when switching scripts. Uses BLOOM-560m perplexity as a proxy.

    Args:
        native_texts (list[str]): Sentences in native script.
        romanized_texts (list[str]): Corresponding romanized sentences.
        model_name (str): HuggingFace model for perplexity computation.

    Returns:
        dict: IP scores and statistics.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

    native_ppl = compute_perplexity(native_texts, model, tokenizer, device)
    roman_ppl = compute_perplexity(romanized_texts, model, tokenizer, device)

    # IP = ratio of information content (inverse perplexity)
    ip_scores = []
    for n_ppl, r_ppl in zip(native_ppl, roman_ppl):
        ip = (1 / n_ppl) / (1 / r_ppl) if r_ppl > 0 else None
        ip_scores.append(ip)

    valid = [s for s in ip_scores if s is not None]
    return {
        "per_sentence_ip": ip_scores,
        "native_perplexities": native_ppl,
        "romanized_perplexities": roman_ppl,
        "mean_ip": float(np.mean(valid)),
        "std_ip": float(np.std(valid)),
    }
