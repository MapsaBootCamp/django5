# import re
#
# text = "12564685312322"
#
# def intcommma(value):
#     org = str(value)
#
#     new = re.sub(r"(-?\d+)(\d{3})", r'\g<1>,\g<2>', org)
#
#     if org == new:
#         return new
#     else:
#         return intcommma(new)
#
#
# print(intcommma(text))
import functools


def my_decorator_with_args(_fun=None,* , age=None):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            if age:
                print("age = ", age)
            func(*args, **kwargs)
            print("Something is happening after the function is called.")
        return wrapper
    if _fun is None:
        return my_decorator
    else:
        return my_decorator(_fun)

def my_decorator2(func):
    def wrapper(*args):
        print("Something is happening before the function is called in 2.")
        func(*args)
        print("Something is happening after the function is called on 2.")
    return wrapper


# @my_decorator2
@my_decorator_with_args
def say_whee(name):
    print("Whee!")

# say_whee = my_decorator2(my_decorator(say_whee))
say_whee("ashkan")
