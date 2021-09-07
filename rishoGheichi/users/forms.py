import re

from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError

from .models import User


class RegisterForm(UserCreationForm):
    error_messages = {
        'phone': _('The two password fields didn’t match.'),
    }

    class Meta:
        model = User
        fields = ("email", "phone")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if re.match(r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}", phone):
            return phone
        else:
            raise ValidationError(
                self.error_messages['phone irani bezan'],
                code='phone',
            )