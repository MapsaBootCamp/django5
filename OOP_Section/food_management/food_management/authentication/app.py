from pathlib import Path
import csv
import hashlib

from food_management.model.Users import UserRegular, UserAdmin
import food_management.config.setting as conf
from food_management.utils import read_csv_return_dict

BASE_DIR = Path(__file__).resolve().parent.parent


def user_exist_check(username: str) -> bool:
    """
    arg: username --> string
    return: bool---> true : user exist, false: user not exist
    """
    csv_data = read_csv_return_dict("user.csv")
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
    hashed_pass = hashlib.sha256(
        password.encode("utf8")).hexdigest()
    users_data = read_csv_return_dict("user.csv")
    for user in users_data:
        if username == user.get("username", None):
            if hashed_pass == user.get("password", None):
                return conf.LOGIN_OK
            else:
                return conf.PASSWORD_INVALID
    return conf.USERNAME_NOT_EXIST


if __name__ == "__main__":
    # print(register("asghar", "1234", "1234"))
    print(login("asgahar", "12345"))
