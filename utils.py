import re
from datetime import datetime as dt


class DateFormatException(Exception):
    """Raise when a specific date is not correctly formated"""

    def __init__(self, message: str, value: [object | None], name: str, *args) -> None:
        self.message = message
        self.value = value
        self.name = name
        super().__init__(message, value, *args)

    def __str__(self) -> str:
        return f"{self.message} for value {self.value} of {self.name}"


def is_date_range_valid(date: str) -> bool:
    """
    Returns True if the date argument is correctly formated according to the format YYYY-MM-DD and the date
    is between 1955 and the past day of today date, otherwise raises DateFormatException error
    """
    pattern = r"[\d]{4}-[\d]{2}-[\d]{2}"
    match = re.match(pattern, date)

    if match == None:
        raise DateFormatException(
            "Date format must be YYYY-MM-DD -> e.g 2000-08-23", date, "date"
        )

    date_format = "%Y-%m-%d"
    today_year = dt.now().year
    today_month = dt.now().month
    today_day = dt.now().day

    current_date = dt.strptime(date, date_format)
    min_date = dt.strptime("1955-11-12", date_format)
    max_date = dt.strptime(f"{today_year}-{today_month}-{today_day - 1}", date_format)

    if current_date < min_date or current_date > max_date:
        return False

    return True

def final_print():
    print("""
Made with ❤️  by Jhonatan Mustiola
Visit him on https://www.github.com/JhonatanMustiolaCas
    """)
