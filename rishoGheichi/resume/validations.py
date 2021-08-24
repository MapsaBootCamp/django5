from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_grade_education(value):
    if value > 20 or value < 0:
        raise ValidationError(
            _('%(value)s is not a(ba tashakor az hossein) good nomreh'),
            params={'value': value},
        )