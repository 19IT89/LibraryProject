import re
import pandas as pd


regex_patterns = {
    "books": {
        "id": r"[\w\W]{12}",
        "title": r"[a-zA-Z0-9]+(?:\s[a-zA-Z0-9]+){0,}",
        "authors": r"\[(?:\'[a-zA-Z\&\.\,\-]+\'\])",
        "publisher": r"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
        "publishedDate": r"[1-2]\d{3}",
        "categories": r"(?:\[(?:\'[\w\W]+\')\])|(?:[a-z]+(?:\s[a-z]+)?)",
        "price": r"\d+[.]\d+",
        "pages": r"\d+"
    },
    "checkouts": {
        "id": r"[\w\W]+",
        "patron_id": r"\w+",
        "library_id": r"\w{3}-\d{3}@\w{3}-\w{3}-\w{3}",
        "date_checkout": r"20\d{2}-(?:0[0-9]|1[0-2])-(?:0[0-9]|[1-2][0-9]|3[0-1])",
        "date_returned": r"20\d{2}-(?:0[0-9]|1[0-2])-(?:0[0-9]|[1-2][0-9]|3[0-1])"

    },
    "customers": {
        "id": r"[\w\W]+",
        "name": r"[a-zA-Z]+(?:\s[a-zA-Z]+){1,3}",
        "street_address": r"\d+\s\w{1,2}\s\w+(?:\s\w+){0,}",
        "city": r"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
        "state": r"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
        "postal_code": r"\d{5}",
        "birth_date": r"(?:19\d{2}|20[0-1]\d)-(?:0[0-9]|1[0-2])-(?:0[0-9]|[1-2][0-9]|3[0-1])",
        "gender":r"male|female|andy|unknown",
        "education": r"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
        "occupation": r"[a-zA-Z]+(?:\s[a-zA-Z]+)?"
    },
    "libraries": {
        "id": r"\w{3}-\d{3}@\w{3}-\w{3}-\w{3}",
        "name": r"[a-zA-Z]{2,}(?:\s[a-zA-Z]{2,}){0,6}",
        "street_address": r"\d+\s\w{1,2}\s\w+(?:\s\w+){0,}",
        "city": r"[a-zA-Z]+(?:\s[a-zA-Z]+)?",
        "state": r"[a-zA-Z]{2,}",
        "postal_code": r"\d{5}"
    }
}


def find_pattern(string: str, regex_pattern: str) -> str|None:
    if type(string) == str:
        output = re.sub(" +", " ", string.lower().strip())
        try:
            output = re.findall(pattern=regex_pattern, string=output)[0]
            return output
        except:
            return None


def find_patterns_in_column(column: pd.Series, df_name: str, col_name: str) -> pd.Series:
    output = column.apply(lambda x: find_pattern(x, regex_patterns[df_name][col_name]))
    return output
