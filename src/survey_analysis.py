"""Statistical analysis helpers for survey-oriented outputs.

Final inferential analysis must be validated against BRFSS weighting documentation.
"""

from __future__ import annotations

import pandas as pd


def weighted_prevalence(df: pd.DataFrame, outcome: str, weight: str) -> float:
    """Compute a simple weighted prevalence estimate.

    This does not by itself account for stratification/PSU variance estimation.
    """
    d = df[[outcome, weight]].dropna()
    return float((d[outcome] * d[weight]).sum() / d[weight].sum())


def weighted_group_prevalence(
    df: pd.DataFrame, group: str, outcome: str, weight: str
) -> pd.DataFrame:
    """Compute simple weighted prevalence by group."""
    def calc(g: pd.DataFrame) -> pd.Series:
        d = g[[outcome, weight]].dropna()
        prev = (d[outcome] * d[weight]).sum() / d[weight].sum()
        return pd.Series({"weighted_prevalence": prev, "n_unweighted": len(d)})

    return df.groupby(group, dropna=False).apply(calc).reset_index()
