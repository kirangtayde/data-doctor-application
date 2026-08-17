import pandas as pd
from src.profiler import profile_dataframe, quality_score

def test_profile():
    df=pd.DataFrame({'a':[1,2,None],'b':['x','x','y']})
    p=profile_dataframe(df)
    assert p.loc[p.column=='a','missing'].iloc[0] == 1
    assert 0 <= quality_score(df) <= 1
