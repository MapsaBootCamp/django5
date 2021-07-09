from pathlib import Path
import csv
import sys

from food_management.model.Users import UserRegular, UserAdmin
import food_management.config.setting as conf

BASE_DIR = Path(__file__).resolve().parent.parent


def user_exist_check(username: str) -> bool:
    """
    arg: username --> string
    return: bool---> true : user exist, false: user not exist
    """

    with open(BASE_DIR / "user.csv") as csvfile:
        csv_data = csv.DictReader(csvfile, delimiter=",")
        for elm in csv_data:
            if username == elm.get("username", None):
                return True
        return False


def register(username, password1, password2) -> int:
    if password1 != password2:
        return conf.PASSWORD_CONFIRMATION_FAILD

    if user_exist_check(username):
        return conf.USERNAME_EXIST
    else:
        user = UserRegular(username, password1)
        user.save()
        return conf.REGISTER_OK


def login(username, password):
    pass


if __name__ == "__main__":
    print(register("asghar", "1234", "1234"))
