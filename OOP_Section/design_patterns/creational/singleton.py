import math as a
import math as b

print("in singleton")

print(id(a))
print(id(b))


class Singlton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        else:
            cls._instance = super().__new__(cls, *args, **kwargs)
            return cls._instance


obj1 = Singlton()
print(id(obj1))
obj2 = Singlton()
print(id(obj2))
