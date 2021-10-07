from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings



@shared_task(name="send_mail")
def async_send_mail(mail_subject, message):
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, ["python.ekbatan@gmail.com"])