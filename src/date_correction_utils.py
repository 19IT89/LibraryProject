import pandas as pd
from dateutil.parser import parse


def parse_date(date: str) -> str|None:
    try:
        return parse(date.strip().replace("%", "").replace("|", "-")).strftime("%Y-%m-%d")
    except:
        return None


def get_wrong_dates_subset(
        input_dataframe: pd.DataFrame,
        corrected_dataframe: pd.DataFrame,
        col_name_incorrect: str,
        col_name_correct: str
) -> pd.DataFrame:
    incorrect_checkouts = corrected_dataframe[col_name_incorrect].isna()
    wrong_dates = pd.concat(
        [
        input_dataframe.loc[incorrect_checkouts, col_name_incorrect].astype("datetime64[ns]"),
        corrected_dataframe.loc[incorrect_checkouts, col_name_correct].astype("datetime64[ns]")
    ],
        axis=1
    )
    return wrong_dates


def correct_checkout_date(row: pd.Series) -> pd.Series:
    output = row.copy()
    checkout_year = row["date_checkout"].year
    returned_year = row["date_returned"].year
    if checkout_year > returned_year:
        output["date_checkout"] = output["date_checkout"].replace(returned_year)
    elif checkout_year < returned_year:
        potential_date = output["date_returned"].replace(returned_year)
        if potential_date >= row["date_returned"]:
            output["date_checkout"] = potential_date.replace(returned_year - 1)
        else:
            output["date_checkout"] = potential_date
    return output


def correct_return_date(row: pd.Series) -> pd.Series:
    output = row.copy()
    checkout_year = row["date_checkout"].year
    returned_year = row["date_returned"].year
    if checkout_year >= returned_year:
        potential_date = output["date_returned"].replace(checkout_year)
        if potential_date <= row["date_checkout"]:
            output["date_returned"] = potential_date.replace(checkout_year + 1)
        else:
            output["date_returned"] = potential_date
    elif returned_year - checkout_year > 1:
        potential_date = output["date_returned"].replace(checkout_year)
        if potential_date <= row["date_checkout"]:
            output["date_returned"] = potential_date.replace(checkout_year + 1)

        else:
            output["date_returned"] = potential_date
    return output


def correct_dates(input_dataframe: pd.DataFrame, corrected_dataframe: pd.DataFrame) -> tuple[
    pd.DataFrame, pd.DataFrame]:
    wrong_checkouts = get_wrong_dates_subset(
        input_dataframe=input_dataframe,
        corrected_dataframe=corrected_dataframe,
        col_name_incorrect="date_checkout",
        col_name_correct="date_returned"
    )

    wrong_returns = get_wrong_dates_subset(
        input_dataframe=input_dataframe,
        corrected_dataframe=corrected_dataframe,
        col_name_incorrect="date_returned",
        col_name_correct="date_checkout"
    )

    corrected_checkouts = wrong_checkouts.apply(lambda row: correct_checkout_date(row), axis=1)
    corrected_returns = wrong_returns.apply(lambda row: correct_return_date(row), axis=1)
    return corrected_checkouts, corrected_returns