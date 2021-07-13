import csv
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent


def create_user_file():
    try:
        with open(BASE_PATH / "user.csv") as f:
            pass
    except IOError:
        fieldnames = ['id', "username", "password",
                      "age", "address", "email", "phone_number", "type"]
        with open(BASE_PATH / "user.csv", 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


if __name__ == "__main__":
    create_user_file()
