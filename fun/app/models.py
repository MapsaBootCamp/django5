from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=250)
    nezam_pezeshki = models.CharField(max_length=150)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.name


class CoronaInforamtion(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    diabet = models.BooleanField()
    feshar_khoon = models.BooleanField()
    charbi_khoon = models.BooleanField()
    talasemi = models.BooleanField()
    tiroid = models.BooleanField()
    sareee = models.BooleanField()
    asm = models.BooleanField()
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
