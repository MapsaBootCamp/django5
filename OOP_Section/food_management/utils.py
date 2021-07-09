import csv
from typing import List, Dict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_csv_return_dict(file_name: str) -> List[Dict]:
    try:
        with open(BASE_DIR / file_name) as csvfile:
            csv_data = csv.DictReader(csvfile, delimiter=",")
            return list(csv_data)
    except IOError as e:
        raise e
