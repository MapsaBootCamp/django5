from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as log_in, logout as log_out
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, CreateView

from utils.verification_email_token_gen import account_activation_token
from .decorators import check_mentor
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


@require_http_methods(["POST"])
def signup(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        if email:
            if User.objects.filter(email__iexact=email).count() == 0:
                password = request.POST.get('password', None)
                repeated_passweord = request.POST.get('repeat_password', None)
                if password:
                    if password == repeated_passweord:
                        try:
                            user = User.objects.create_user(email=email, password=password, phone=phone,
                                                            is_active=False)
                            current_site = get_current_site(request)
                            mail_subject = 'Activate your account in RishoGheichi.'
                            message = render_to_string('validation_email_template.html', {
                                'user': user,
                                'domain': current_site.domain,
                                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                'token': account_activation_token.make_token(user),
                            })
                            to_email = request.POST.get('email')
                            send_mail(mail_subject, message, settings.EMAIL_HOST_USER, ["python.ekbatan@gmail.com"])
                            return HttpResponse('Please confirm your email address to complete the registration')
                            messages.success(request, "Register Successfully!")
                            return redirect('/')
                        except IntegrityError as e:
                            # return render(request, "user/error.html", {"message": e})
                            messages.error(request, f"{e}")
                            return redirect('user-view')
                    else:
                        return HttpResponse("pass va tekraresh equal nistan")
            else:
                return HttpResponse("email tekrari")


def email_activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = RegisterForm
    success_url = '/account/login'




def check_khodia(user):
    if user.is_authenticated:
        return user.email.endswith('@rishogheichi.com')
    return False


@user_passes_test(check_khodia, login_url='/account/login')
def faghat_khodia(request):
    return HttpResponse("raghs bandari")


@permission_required("course.raghs_bandari", raise_exception=True)
@login_required
def raghas_khune(request):
    return HttpResponse("baba karam!")


@check_mentor(age=21)
def poya_irad_bani_esraeil(request):
    return HttpResponse("man mentoram")