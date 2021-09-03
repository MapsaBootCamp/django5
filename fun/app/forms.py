from django import forms
from django.core.exceptions import ValidationError

from .models import CoronaInforamtion


def validate_email(value):
    print("hellllllo")
    if "ashkan" in value:
        raise ValidationError(
            'Invalid value: %(value)s',
            code='invalid',
        )


class CoronaInfoForm(forms.ModelForm):

    class Meta:
        model = CoronaInforamtion
        fields = "__all__"

    def clean_email(self):
        data = self.cleaned_data['email']
        if "ashkan" in data:
            raise ValidationError(
                f'Invalid value: {data}',
                code='invalid',
            )
        return data

    def clean(self):
        talasemi = self.cleaned_data['talasemi']
        tiroid = self.cleaned_data['tiroid']

        if talasemi and tiroid:
            raise ValidationError(
                f'Khaili band: adam hamzaman takasemi tiroid nemigire',
                code='invalid',
            )

        return self.cleaned_data
