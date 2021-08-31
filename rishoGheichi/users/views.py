from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log_in, logout as log_out


def login(request):
    if request.method == "GET":
        return render(request, "login.html", {})
    elif request.method == "POST":
        email = request.POST.get("email", None)
        if not email:
            return render(request, "404.html", {})
        password = request.POST.get("password", None)
        if not password:
            return render(request, "404.html", {})
        user = authenticate(username=email, password=password)
        if user:
            log_in(request, user)
            return HttpResponse("Khosh Amadi")
        else:
            return HttpResponse("matasefane nashod")
    return render(request, "404.html", {})


def logout(request):
    pass


def register(request):
    pass
