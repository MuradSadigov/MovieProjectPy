import re
import os
from enum import Enum

ABSOLUTE_PATH = os.path.dirname(__file__)
MIN_YEAR = 1800


class Tables(Enum):
    movies = "movies"
    actors = "actors"
    participation = "participation"


def get_file_path(file_name: str) -> str:
    return os.path.join(ABSOLUTE_PATH, "schemas", f"{file_name}.sql")


def read_file(file_name: str) -> str:
    try:
        with open(get_file_path(file_name), "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Check the file path.")


def minutes_to_time_format(minuntes: int) -> str:
    hours, min = divmod(minuntes, 60)
    return f"{hours:02d}:{min:02d}"


def time_format_to_minutes(time_str: str) -> int:
    duration = time_str.split(":")
    return int(duration[0]) * 60 + int(duration[1])


def is_valid_year(year: str) -> bool:
    return year.isdigit() and MIN_YEAR <= int(year)


def is_valid_time_format(time_str: str) -> bool:
    pattern = re.compile(r'^[0-9][0-9]:[0-5][0-9]$')
    return bool(pattern.match(time_str))
