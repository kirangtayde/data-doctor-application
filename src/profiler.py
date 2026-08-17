from __future__ import annotations
import pandas as pd

def profile_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    rows=[]
    for c in df.columns:
        s=df[c]
        rows.append({'column':c,'dtype':str(s.dtype),'rows':len(s),'missing':int(s.isna().sum()),'missing_pct':float(s.isna().mean()*100),'unique':int(s.nunique(dropna=True)),'duplicate_values':int(s.duplicated().sum())})
    return pd.DataFrame(rows)

def quality_score(df: pd.DataFrame) -> float:
    missing_penalty=float(df.isna().mean().mean())
    duplicate_penalty=float(df.duplicated().mean())
    return max(0.0,1.0-missing_penalty-duplicate_penalty)
