import uuid
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
        with open(BASE_PATH + "user", 'a', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


    def _set_id(self, id):
        if id:
            return id
        else:
            str(uuid.uuid4)


class UserAddi(User):
    _type = "active"


class UserAdmin(User):
    _type = "staff"
