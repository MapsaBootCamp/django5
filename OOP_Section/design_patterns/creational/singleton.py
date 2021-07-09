# import math as a
# import math as b

# print("in singleton")

# print(id(a))
# print(id(b))


# class Singlton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance:
#             return cls._instance
#         else:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             return cls._instance


# obj1 = Singlton()
# print(id(obj1))
# obj2 = Singlton()
# print(id(obj2))


class Meta(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance

        print(Meta._instance)
        return cls._instance[cls]


class MySingleton1(metaclass=Meta):
    pass


class MySingleton2(metaclass=Meta):
    pass