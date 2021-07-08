class User:
    _type = None

    def __init__(self, username, password, age=None, phone_number=None, address = None, email= None):
        self.username = username
        self.password = password
        self.age = age 
        self.phone_number = phone_number
        self.address = address
        self.email = email


class UserAddi(User):
    _type = "addi"


class UserAdmin(User):
    _type = "admin"





