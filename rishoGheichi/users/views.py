from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as log_in, logout as log_out
from django.db import IntegrityError
from django.views.generic import FormView

from .forms import RegisterForm

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        if email:
            password = request.POST.get('password', None)
            if password:
                user = authenticate(request, email=email, password=password)
                if user:
                    log_in(request, user)
                    messages.error(request, 'welcome!')
                    if request.GET.get('next_url', None):
                        return redirect(request.GET.get('next_url'))
                    return redirect("/admin/")
                else:
                    return HttpResponse("user pass eshtebah")
        else:
            return HttpResponse("email ro bezar")
    else:
        next_url = request.GET.get('next', "/")
        return render(request, 'users/login-register.html', {"next_url": next_url})


def logout_view(request):
    log_out(request)
    return redirect('/')


def signup(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        if email:
            password = request.POST.get('password', None)
            repeated_passweord = request.POST.get('repeat_password', None)
            if password:
                if password == repeated_passweord:
                    try:
                        User.objects.create_user(email=email, password=password, phone=phone)
                        messages.success(request, "Register Successfully!")
                        return redirect('/')
                    except IntegrityError as e:
                        # return render(request, "user/error.html", {"message": e})
                        messages.error(request, f"{e}")
                        return redirect('user-view')
                else:
                    return HttpResponse("pass va tekraresh equal nistan")


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = RegisterForm


def check_khodia(user):
    if user.is_authenticated:
        return user.email.endswith('@rishogheichi.com')
    return False


@user_passes_test(check_khodia, login_url='/account/login')
def faghat_khodia(request):
    return HttpResponse("raghs bandari")