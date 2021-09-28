from django.db import models
from django.contrib.auth import get_user_model

from resume.validations import validate_grade_education

User = get_user_model()


class WorkExprience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500)
    position = models.CharField(max_length=500)
    modat_zaman = models.IntegerField()
    description = models.TextField()


class Educations(models.Model):
    MAGHTA_CHOICES = (
        ('k', 'karshenasi'),
        ('a', 'arshad'),
        ('d', 'doctora'),
        ('p', 'pasa doctora')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=500)
    maghta = models.CharField("مقطع تحصیلی", max_length=1, choices=MAGHTA_CHOICES)
    grade = models.FloatField(validators=[validate_grade_education])
