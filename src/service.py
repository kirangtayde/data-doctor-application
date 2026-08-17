from __future__ import annotations
import pandas as pd
from .profiler import profile_dataframe, quality_score
from .rules import validate_required_columns, validate_ranges

def diagnose(df: pd.DataFrame, required=None, ranges=None) -> dict:
    required=required or []; ranges=ranges or {}
    return {'quality_score':quality_score(df),'profile':profile_dataframe(df).to_dict(orient='records'),'required':validate_required_columns(df,required),'ranges':validate_ranges(df,ranges)}
