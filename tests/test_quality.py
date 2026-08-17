import pandas as pd

from src.quality import profile_dataframe


def test_profile_dataframe_reports_missingness_and_uniques():
    df = pd.DataFrame({"age": [10, None, 10], "city": ["Pune", "Mumbai", "Pune"]})
    result = profile_dataframe(df).set_index("column")
    assert result.loc["age", "missing_count"] == 1
    assert result.loc["city", "unique_count"] == 2
