from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# functional view


def hello_django(request):
    a = 2
    b = 3
    response = HttpResponse(f"salam mapsa {a+b} martabe")
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path("salam/", hello_django),
    path("app/", include("app.urls"))
]
