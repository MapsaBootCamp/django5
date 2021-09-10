import time

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MahramanehMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.cart = "mentor"
        # return HttpResponse("salam")
        # raise Exception("mojaz nisi")

    def process_view(self, request, view_fun, *args):
        print("salam in view")
        # return view_fun(request, id)

        # print("salam view")
        # print(args)
        # print(view_fun.__name__)
        # print(view_fun.__module__)
        
    # def process_response(self, request, response):
    #     # return HttpResponse("salam")
    #     return None



    