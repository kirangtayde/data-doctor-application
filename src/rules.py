from __future__ import annotations
import pandas as pd

def validate_required_columns(df: pd.DataFrame, required: list[str]) -> list[dict]:
    return [{'rule':'required_columns','status':'pass' if c in df.columns else 'fail','column':c} for c in required]

def validate_ranges(df: pd.DataFrame, ranges: dict[str, tuple[float,float]]) -> list[dict]:
    findings=[]
    for c,(lo,hi) in ranges.items():
        if c not in df: findings.append({'column':c,'status':'missing_column'}); continue
        bad=((df[c]<lo)|(df[c]>hi)).sum()
        findings.append({'column':c,'status':'pass' if bad==0 else 'fail','violations':int(bad),'min':lo,'max':hi})
    return findings

def diagnosis_report(df: pd.DataFrame, required=None, ranges=None) -> dict:
    return {'quality_score':quality_score(df),'required':validate_required_columns(df,required or []),'ranges':validate_ranges(df,ranges or {})}

from .profiler import quality_score
