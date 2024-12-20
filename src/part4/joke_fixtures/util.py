import csv
from typing import Any


def from_csv_to_dict(filepath: str) -> list[dict[Any, Any]]:
    with open(filepath, encoding="utf8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data
