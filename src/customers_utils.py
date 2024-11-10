import pandas as pd
from gender_guesser.detector import Detector


# gender detector
gender_detector = Detector()


def detect_gender(name: str) -> str:
    gender = gender_detector.get_gender(name.capitalize())
    if gender in ["mostly_male", "mostly_female"]:
        return gender.split("_")[1]
    if gender in ["unknown", "andy"]:
        return "unknown"
    return gender


def detect_gender_row(row: pd.Series) -> pd.Series:
    output = row.copy()
    output["gender"] = detect_gender(name=row["name"].split(" ")[0])
    return output


def fill_education_and_occupation(row: pd.Series, education_groups, occupation_groups) -> pd.Series:
    education = row["education"]
    occupation = row["occupation"]
    gender = row["gender"]
    output = row.copy()
    if (education is None) and (occupation is not None):
        output["education"] = occupation_groups.get_group((occupation, gender)).mode().iloc[0]
    elif (education is not None) and (occupation is None):
        output["occupation"] = education_groups.get_group((education, gender)).mode().iloc[0]
    return output
