from functools import wraps

from django.http import HttpResponse


def check_mentor(_fun=None,* , age=None):
    def my_decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.cart == "mentor":
                if age > 20:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("shma jooje mentori")
            else:
                return HttpResponse("mentor nisi")
        return wrapper
    if _fun is None:
        return my_decorator
    else:
        return my_decorator(_fun)
