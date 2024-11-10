import pandas as pd
from src.regex_patterns import regex_patterns


def count_nan(df: pd.DataFrame) -> int:
    return df.isnull().sum()


def aggregate_columns(df: pd.DataFrame) -> pd.DataFrame:
    output = df.agg(["nunique", count_nan]).transpose()
    output.index.name = "column name"
    return output


def count_matching_rows(df: pd.DataFrame, group: str, skip: list[str]|None = None) -> pd.Series:
    if skip is None:
        skip = []
    output = pd.Series()
    for key, pattern in regex_patterns[group].items():
        if  not key in skip:
            current_col = df[key].astype('string')
            output[key] = int(current_col.str.match("(?i)^" + pattern + "$").sum())
    return output


def describe_data(df_dict: dict[str, pd.DataFrame], skip: list[str]|None = None) -> tuple[pd.DataFrame, pd.Series]:
    if skip is None:
        skip = []
    raw_data_description = {}
    for key, dataframe in df_dict.items():
        raw_data_description[key] = aggregate_columns(df=dataframe)
        raw_data_description[key]["regex_match"] = count_matching_rows(df=dataframe, group=key, skip=skip)
    column_description = pd.concat(raw_data_description.values(), keys=raw_data_description.keys())

    # dataframe row counts
    row_counts = pd.Series({key: len(dataframe) for key, dataframe in df_dict.items()}, name="row counts")
    return column_description, row_counts