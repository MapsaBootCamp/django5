from typing import List


# class ClassName:
#     # attribute
#     # method


class Machine:  # class Machine(object):
    count = 0  # class atribute

    # dunder method or magic method
    def __init__(self, color, door_num, double_usage, sun_roof=False):
        self.color = color
        self.door_num = door_num
        self.double_usage = double_usage
        self.sun_roof = sun_roof
        self.tire_brand = None
        Machine.count += 1

    def __new__(cls, *args, **kwargs):
        instance = super(Machine, cls).__new__(cls, *args, **kwargs)
        return instance

    @classmethod
    def test_class_method(cls):
        pass

    def engine(self):
        pass

    def change_usage_duality(self):
        self.double_usage = not self.double_usage

    def print_color(self):
        print(self.color)

    @staticmethod
    def company_time_work():
        print("az sob ta asr")


# class A:
#     __name = "ashkan"
#     my_data = []

#     def print_hello(self):
#         print(f"hello {self.__name}")

#     def __partibazi(self):
#         print("Ok!!")

#     def __test_private(self):
#         self.__partibazi()

#     def add_data(self) -> List:
#         self.my_data.append(10)
#         return self.my_data


# class B:
#     # def print_hello(self):
#     #     print("hello b")

#     def test_private_A_in_B(self):
#         self.__partibazi()

#     def hello_b(self):
#         print("hello im in B")


# class C(A, B):
#     def print_hello(self):
#         super().print_hello()
#         print("salam man c am")

#     def shalgham(self):
#         super().print_hello()

#     def add_data(self) -> List:
#         data = super().add_data()
#         print(data)
#         data.append(12)
#         return data


# a = A()
# print(a._A__name)
# a.print_hello()
# a._A__partibazi()

# b = B()
# b.print_hello()
# b.test_private_A_in_B()
# b.__partibazi()
# c = C()
# c.hello_b()
# c.print_hello()
# print(c.add_data())

# machine1 = Machine("red", 2, False)
# machine1.print_color()
# machine2 = Machine("white", 4, True)
# machine2.print_color()
# machine1.change_usage_duality()
# print(machine1.double_usage)
# machine1.company_time_work()

class AMetaClass(type):
    def __call__(self):
        print("in call metaclass")
        return super().__call__()


class A(metaclass=AMetaClass):
    def __init__(self):
        print("in init")

    def __new__(cls, *args, **kwargs):
        print("in new")
        instance = super(A, cls).__new__(cls, *args, **kwargs)
        return instance

    def __call__(self):
        print("im in call")

    def __str__(self):
        return "print shode object"

# inheritance vs metaclass


a = A()
a()
print(a)
print(type(a))
print(isinstance(A, type))


print("class object is instance of type: ", isinstance(object, type))
print("class type is instance of object: ", isinstance(type, object))
print("class object is subcless of type: ", issubclass(object, type))
print("class type is subclass of object: ", isinstance(type, object))
