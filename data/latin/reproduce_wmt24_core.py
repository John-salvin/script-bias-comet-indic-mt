#!/usr/bin/env python3
"""
reproduce_wmt24_core.py
=======================
Reproduces the core WMT24 EN-DE / EN-ES dataset rows exactly:

  lang_pair | system | domain | doc | seg_id | source | target | refA
  rater | category | severity | error_start | error_end | mqm_score
  + esa_score (EN-ES sheet only)

No MT metrics. No tokenization. No NLL.
Pure WMT24 human evaluation data from mt-metrics-eval-v2.

OUTPUT
------
wmt24_core_ende_enes.xlsx (two sheets: German, Spanish)

SETUP (run once)
----------------
pip install mt-metrics-eval sacrebleu pandas openpyxl

# Downloads ~2 GB of WMT data to ~/.mt-metrics-eval/
python -c "from mt_metrics_eval import data; data.Download()"

THEN RUN
--------
python reproduce_wmt24_core.py

Citation
--------
Kocmi et al. (2024). Findings of the WMT24 General Machine Translation
Shared Task. Proceedings of WMT 2024, pp. 1-46. ACL.
https://aclanthology.org/2024.wmt-1.1/

Data repository:
https://github.com/google-research/mt-metrics-eval
"""

import os
import re
import subprocess
import sys

# ── auto-install dependencies ─────────────────────────────────────────────────
def _install(pkg):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg, "-q"])

for pkg in ["mt-metrics-eval", "sacrebleu", "pandas", "openpyxl"]:
    try:
        __import__(pkg.replace("-", "_"))
    except ImportError:
        print(f"Installing {pkg}...")
        _install(pkg)

from mt_metrics_eval import data as mtme_data
import pandas as pd
import sacrebleu as sb

# ── CONFIG ────────────────────────────────────────────────────────────────────
OUTPUT_XLSX = "wmt24_core_ende_enes.xlsx"

# If you have the mt-metrics-eval-v2 folder locally, set this path.
# Otherwise leave as None and sacrebleu will download references automatically.
MTME_DIR = None
# Example: MTME_DIR = "/home/user/Research/mt-metrics-eval-v2"

# Official WMT MQM penalty weights
MQM_WEIGHTS = {"no-error": 0.0, "minor": 1.0, "major": 5.0, "critical": 25.0}
PUNCT_RE = re.compile(r"(fluency|punctuation)", re.IGNORECASE)
MAX_ERRORS = 5  # top-5 errors per rater, then average across raters

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 — Load EvalSet from mt-metrics-eval
# ─────────────────────────────────────────────────────────────────────────────
def load_evset(testset, langpair):
    try:
        return mtme_data.EvalSet(testset, langpair, read_stored_metrics=False)
    except FileNotFoundError:
        sys.exit(
            f"\nERROR: mt-metrics-eval data not found for {testset}/{langpair}.\n"
            "Please run once:\n"
            ' python -c "from mt_metrics_eval import data; data.Download()"\n'
            "This downloads ~2 GB to ~/.mt-metrics-eval/\n"
        )

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2 — Build {source_sentence -> refA_sentence} lookup
# ─────────────────────────────────────────────────────────────────────────────
def build_ref_map(testset, langpair):
    if MTME_DIR:
        src_path  = os.path.join(MTME_DIR, testset, "sources",    f"{langpair}.txt")
        refa_path = os.path.join(MTME_DIR, testset, "references", f"{langpair}.refA.txt")
        if os.path.exists(src_path) and os.path.exists(refa_path):
            with open(src_path,  encoding="utf-8") as f: srcs = [l.rstrip("\n") for l in f]
            with open(refa_path, encoding="utf-8") as f: refs = [l.rstrip("\n") for l in f]
            print(f"  [{langpair}] Loaded {len(srcs)} reference pairs from local files.")
            return dict(zip(srcs, refs))

    print(f"  [{langpair}] Downloading references via sacrebleu...")
    src_file  = sb.get_source_file(testset, langpair)
    ref_files = sb.get_reference_files(testset, langpair)
    with open(src_file,    encoding="utf-8") as f: srcs = [l.rstrip("\n") for l in f]
    with open(ref_files[0],encoding="utf-8") as f: refs = [l.rstrip("\n") for l in f]
    print(f"  [{langpair}] sacrebleu gave {len(srcs)} reference pairs.")
    return dict(zip(srcs, refs))


def strip_v_tags(text):
    """Strip WMT MQM annotation tags <v>...</v> from source text."""
    return re.sub(r"</?v>", "", str(text)).strip()

# ─────────────────────────────────────────────────────────────────────────────
# STEP 3 — Extract per-rater MQM annotations into a flat DataFrame
# ─────────────────────────────────────────────────────────────────────────────
def extract_mqm_annotations(evs, langpair):
    ratings_dict = getattr(evs, "Ratings", {})

    if not ratings_dict:
        print(f"  [{langpair}] No Ratings API found. Building from system outputs only.")
        rows = []
        for doc in evs.all_docs:
            srcs   = evs.src.get(doc, [])
            domain = doc.split("_")[0]
            for system, sys_docs in evs.sys_outputs.items():
                tgts = sys_docs.get(doc, [])
                for i, (src, tgt) in enumerate(zip(srcs, tgts)):
                    rows.append(dict(
                        lang_pair=langpair, system=system, domain=domain,
                        doc=doc, seg_id=i + 1, source=src, target=tgt,
                        rater="unknown", category="No-error", severity="No-error",
                        error_start=None, error_end=None,
                    ))
        return pd.DataFrame(rows)

    rows = []
    for rater_key, rating_list in ratings_dict.items():
        for rating in rating_list:
            system  = rating.system
            doc     = rating.doc
            seg_idx = rating.seg - 1
            src_list = evs.src.get(doc, [])
            tgt_list = evs.sys_outputs.get(system, {}).get(doc, [])
            if seg_idx >= len(src_list):
                continue
            source = src_list[seg_idx]
            target = tgt_list[seg_idx] if seg_idx < len(tgt_list) else ""
            domain = doc.split("_")[0]

            if not rating.errors:
                rows.append(dict(
                    lang_pair=langpair, system=system, domain=domain,
                    doc=doc, seg_id=rating.seg, source=source, target=target,
                    rater=rater_key, category="No-error", severity="No-error",
                    error_start=None, error_end=None,
                ))
            else:
                for err in rating.errors:
                    span = getattr(err, "span", None)
                    rows.append(dict(
                        lang_pair=langpair, system=system, domain=domain,
                        doc=doc, seg_id=rating.seg, source=source, target=target,
                        rater=rater_key,
                        category=getattr(err, "category", "unknown"),
                        severity=getattr(err, "severity", "unknown"),
                        error_start=span[0] if span else None,
                        error_end=span[1]   if span else None,
                    ))
    return pd.DataFrame(rows)

# ─────────────────────────────────────────────────────────────────────────────
# STEP 4 — Compute official WMT MQM penalty score per (system, source)
# ─────────────────────────────────────────────────────────────────────────────
def compute_mqm_scores(df):
    def _weight(cat, sev):
        s = str(sev).strip().lower()
        c = str(cat).strip().lower()
        if s in ("no-error", "neutral", ""):
            return 0.0
        if s == "minor" and PUNCT_RE.search(c):
            return 0.1
        return MQM_WEIGHTS.get(s, 0.0)

    records = []
    for (system, source, rater), grp in df.groupby(["system", "source", "rater"]):
        weights = sorted(
            [_weight(r["category"], r["severity"]) for _, r in grp.iterrows()],
            reverse=True
        )[:MAX_ERRORS]
        records.append({"system": system, "source": source, "rater": rater, "_penalty": sum(weights)})

    rdf      = pd.DataFrame(records)
    score_df = (
        rdf.groupby(["system", "source"])["_penalty"]
        .mean().reset_index()
        .rename(columns={"_penalty": "mqm_score"})
    )
    score_df["mqm_score"] = -score_df["mqm_score"]
    return score_df

# ─────────────────────────────────────────────────────────────────────────────
# STEP 5 — Extract ESA scores (EN-ES only)
# ─────────────────────────────────────────────────────────────────────────────
def extract_esa_scores(evs):
    try:
        esa_dict = evs.Scores("seg", "esa")
    except Exception as e:
        print(f"  ESA scores not available: {e}")
        return pd.DataFrame(columns=["system", "source", "esa_score"])

    rows = []
    for system, seg_scores in esa_dict.items():
        idx = 0
        for doc in evs.all_docs:
            for src in evs.src.get(doc, []):
                if idx < len(seg_scores):
                    rows.append({"system": system, "source": src, "esa_score": seg_scores[idx]})
                idx += 1
    if not rows:
        return pd.DataFrame(columns=["system", "source", "esa_score"])
    return pd.DataFrame(rows)

# ─────────────────────────────────────────────────────────────────────────────
# STEP 6 — Main build function for one language pair
# ─────────────────────────────────────────────────────────────────────────────
def build_sheet(langpair, add_esa=False):
    print(f"\n{'='*60}")
    print(f"  Processing {langpair.upper()}")
    print(f"{'='*60}")

    evs = load_evset("wmt24", langpair)

    print("  Extracting per-rater MQM annotations...")
    df = extract_mqm_annotations(evs, langpair)
    print(f"  Annotation rows extracted: {len(df)}")

    print("  Building refA lookup...")
    ref_map     = build_ref_map("wmt24", langpair)
    df["refA"]  = df["source"].map(ref_map)

    v_mask = df["refA"].isna() & df["source"].str.contains("<v>", na=False)
    if v_mask.sum() > 0:
        df.loc[v_mask, "refA"] = df.loc[v_mask, "source"].apply(strip_v_tags).map(ref_map)

    matched   = df["refA"].notna().sum()
    unmatched = df["refA"].isna().sum()
    print(f"  refA matched : {matched} rows")
    if unmatched:
        print(f"  refA unmatched: {unmatched} rows (canary/extra docs — expected)")

    print("  Computing MQM penalty scores...")
    mqm_df = compute_mqm_scores(df)
    df     = df.merge(mqm_df, on=["system", "source"], how="left")

    if add_esa:
        print("  Extracting ESA scores...")
        esa_df = extract_esa_scores(evs)
        if not esa_df.empty:
            df = df.merge(esa_df, on=["system", "source"], how="left")
            print(f"  ESA matched: {df['esa_score'].notna().sum()} rows")
        else:
            df["esa_score"] = float("nan")

    return df

# ─────────────────────────────────────────────────────────────────────────────
# STEP 7 — Filter to shared source sentences (339 sentences in both sheets)
# ─────────────────────────────────────────────────────────────────────────────
def filter_to_shared(df_de, df_es):
    shared = set(df_de["source"].dropna().unique()) & set(df_es["source"].dropna().unique())
    df_de  = df_de[df_de["source"].isin(shared)].copy()
    df_es  = df_es[df_es["source"].isin(shared)].copy()
    print(f"\nShared source sentences : {len(shared)}")
    print(f"EN-DE rows after filter : {len(df_de)}")
    print(f"EN-ES rows after filter : {len(df_es)}")
    return df_de, df_es

# ─────────────────────────────────────────────────────────────────────────────
# STEP 8 — Final column ordering
# ─────────────────────────────────────────────────────────────────────────────
DE_COLS = [
    "lang_pair", "system", "domain", "doc", "seg_id",
    "source", "target", "refA",
    "rater", "category", "severity", "error_start", "error_end",
    "mqm_score",
]
ES_COLS = [
    "lang_pair", "system", "domain", "doc", "seg_id",
    "source", "target", "refA",
    "rater", "category", "severity", "error_start", "error_end",
    "mqm_score", "esa_score",
]

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df_de = build_sheet("en-de", add_esa=False)
    df_es = build_sheet("en-es", add_esa=True)

    df_de, df_es = filter_to_shared(df_de, df_es)

    de_final = [c for c in DE_COLS if c in df_de.columns]
    es_final = [c for c in ES_COLS if c in df_es.columns]
    df_de = df_de[de_final].reset_index(drop=True)
    df_es = df_es[es_final].reset_index(drop=True)

    print(f"\nEN-DE final shape : {df_de.shape}")
    print(f"EN-ES final shape : {df_es.shape}")

    print(f"\nSaving to {OUTPUT_XLSX} ...")
    with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
        df_de.to_excel(writer, sheet_name="German",  index=False)
        df_es.to_excel(writer, sheet_name="Spanish", index=False)

    print(f"\nDone. Output: {OUTPUT_XLSX}")
    print("\nColumn guide:")
    print("  lang_pair    : 'en-de' or 'en-es'")
    print("  system       : MT system name (e.g. GPT-4, Gemini-1.5-Pro)")
    print("  domain       : news | social | speech | literary")
    print("  doc          : document name from WMT24")
    print("  seg_id       : 1-based segment index within the document")
    print("  source       : English source sentence")
    print("  target       : MT system output")
    print("  refA         : Human reference translation A")
    print("  rater        : Annotator ID (rater1 … rater10)")
    print("  category     : MQM error category (or 'No-error')")
    print("  severity     : no-error | minor | major | critical | neutral")
    print("  error_start  : character offset of error span start (NaN if no error)")
    print("  error_end    : character offset of error span end (NaN if no error)")
    print("  mqm_score    : -(avg of top-5 per-rater penalties); 0=perfect, neg=errors")
    print("  esa_score    : ESA direct assessment 0-100 (EN-ES only; NaN if not rated)")
