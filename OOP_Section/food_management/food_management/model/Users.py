import uuid
import hashlib
import csv
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent.parent


class User:
    _type = None
    _file_path = BASE_PATH

    def __init__(self, username, password, age=None, phone_number=None, address=None, email=None, id=None):
        self.id = self._set_id(id)
        self.username = username
        self.password = password
        self.age = age
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def save(self):
        self.password = hashlib.sha256(
            self.password.encode("utf8")).hexdigest()
        with open(BASE_PATH / "user.csv", 'a', newline='') as csvfile:
            fieldnames = ['id', "username", "password",
                          "age", "address", "email", "phone_number", "type"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': self.id, "username": self.username, "password": self.password,
                             "age": self.age, "address": self.address, "email": self.email, "phone_number": self.phone_number, "type": self._type})

    def _set_id(self, id):
        if id:
            return id
        else:
            return str(uuid.uuid4())


class UserRegular(User):
    _type = "active"


class UserAdmin(User):
    _type = "staff"


if __name__ == "__main__":
    user = UserAdmin("ashkan", "1234", age=2)
    user.save()
