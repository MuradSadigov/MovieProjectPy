import os

ABSOLUTE_PATH = os.path.dirname(__file__)


def get_file_path(file_name: str) -> str:
    return os.path.join(ABSOLUTE_PATH, "schemas", f"{file_name}.sql")


def read_file(file_name: str) -> str:
    try:
        with open(get_file_path(file_name), "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Check the file path.")
