"""Preprocessing helpers for the QM640 BRFSS capstone."""

from __future__ import annotations

import pandas as pd


def load_brfss_xpt(path: str) -> pd.DataFrame:
    """Load the CDC BRFSS SAS Transport file."""
    return pd.read_sas(path, format="xport")


def select_project_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return the project analysis columns available in the raw file."""
    columns = [
        "_MICHD",
        "_AGEG5YR",
        "_SEX",
        "_RACEGR3",
        "_EDUCAG",
        "_INCOMG1",
        "_BMI5",
        "_BMI5CAT",
        "_SMOKER3",
        "_TOTINDA",
        "DIABETE4",
        "GENHLTH",
        "MENTHLTH",
        "_LLCPWT",
        "_STSTR",
        "_PSU",
    ]
    available = [c for c in columns if c in df.columns]
    return df.loc[:, available].copy()


def recode_outcome(df: pd.DataFrame) -> pd.DataFrame:
    """Map _MICHD to 1/0 and drop non-definitive outcome values."""
    out = df.copy()
    out["chd_mi"] = out["_MICHD"].map({1: 1, 2: 0})
    return out


def missingness_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return count and percentage missing by variable."""
    n = len(df)
    return pd.DataFrame({
        "missing_n": df.isna().sum(),
        "missing_pct": (df.isna().mean() * 100).round(2),
        "non_missing_n": n - df.isna().sum(),
    }).sort_values("missing_pct", ascending=False)
