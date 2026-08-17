from __future__ import annotations

import pandas as pd


def profile_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Return a compact, model-ready data-quality profile."""
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    rows = []
    for column in df.columns:
        series = df[column]
        rows.append(
            {
                "column": column,
                "dtype": str(series.dtype),
                "missing_count": int(series.isna().sum()),
                "missing_pct": float(series.isna().mean()),
                "unique_count": int(series.nunique(dropna=True)),
                "duplicate_values": int(series.duplicated(keep=False).sum()),
            }
        )
    return pd.DataFrame(rows)
