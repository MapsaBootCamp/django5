import re

from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError

from .models import User


class RegisterForm(UserCreationForm):
    error_messages = {
        'phone': _('Phone pattern not matched.'),
    }

    class Meta:
        model = User
        fields = ("email", "phone")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if re.match(r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}", phone):
            return phone
        else:
            print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!")
            raise ValidationError("phone irani bezan masalan: 09121212345")