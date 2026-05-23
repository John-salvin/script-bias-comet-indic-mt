#!/usr/bin/env python3
"""fix_xlsx_headers.py

One-time script to repair the three header issues in
Information_parity_outputs_all.xlsx that cannot be applied via GitHub's
binary file API:

  C1. Tamil sheet col 0: Amazon URL → 'ID (ignore_column)'
  C2. Malayalam sheet: rename 'Chrf' → 'chrF', drop 'Unnamed: 18'
  C3. Drop 'comet_qe_romanized' from HIN and TAM sheets
      (GUJ/MAL/MAR lack it; dropping keeps the schema uniform)

Usage:
  python data/scripts/fix_xlsx_headers.py \\
      --xlsx data/processed/Information_parity_outputs_all.xlsx
"""

import argparse
from pathlib import Path
import pandas as pd


def fix(xlsx_path: Path) -> None:
    print(f"Reading {xlsx_path} ...")
    sheets = pd.read_excel(xlsx_path, sheet_name=None)

    # C1 — Tamil: first column header is an Amazon URL
    if "Tamil" in sheets:
        df = sheets["Tamil"]
        first_col = df.columns[0]
        if str(first_col).startswith("http"):
            df = df.rename(columns={first_col: "ID (ignore_column)"})
            print(f"  Tamil: col 0 renamed '{first_col}' → 'ID (ignore_column)'")
        sheets["Tamil"] = df

    # C2 — Malayalam: Chrf → chrF, drop Unnamed: 18
    if "Malayalam" in sheets:
        df = sheets["Malayalam"]
        if "Chrf" in df.columns:
            df = df.rename(columns={"Chrf": "chrF"})
            print("  Malayalam: 'Chrf' → 'chrF'")
        unnamed_cols = [c for c in df.columns if str(c).startswith("Unnamed: 18")]
        if unnamed_cols:
            df = df.drop(columns=unnamed_cols)
            print(f"  Malayalam: dropped {unnamed_cols}")
        sheets["Malayalam"] = df

    # C3 — Drop comet_qe_romanized from HIN and TAM
    for lang in ("Hindi", "Tamil"):
        if lang in sheets:
            df = sheets[lang]
            if "comet_qe_romanized" in df.columns:
                df = df.drop(columns=["comet_qe_romanized"])
                print(f"  {lang}: dropped 'comet_qe_romanized'")
            sheets[lang] = df

    # Write back
    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        for sheet_name, df in sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Done. Saved → {xlsx_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Fix xlsx header issues.")
    ap.add_argument(
        "--xlsx",
        default="data/processed/Information_parity_outputs_all.xlsx",
        help="Path to the workbook (default: data/processed/Information_parity_outputs_all.xlsx)",
    )
    args = ap.parse_args()
    fix(Path(args.xlsx))
