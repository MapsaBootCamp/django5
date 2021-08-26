from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from utils.models_utils import model_image_directory_path
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, phone="", **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_mentoruser(self, email, password, phone="",  **extra_fields):
        """
          Create and save a Mentor with the given email and password.
          """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin user must have is_staff=True.')
        return self.create_user(email, password,phone, **extra_fields)

    def create_superuser(self, email, password, phone="",  **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password,phone, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=250)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserhayeMoredeAlagheMardani(User):
    leader = models.CharField(max_length=50, default="fatemeh mardani")

    class Meta:
        verbose_name = _('mardani_user')
        verbose_name_plural = _('mardani_users')

class BaseKarbaran(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=model_image_directory_path)

    class Meta:
        abstract = True


class Karjoo(BaseKarbaran):
    pass


class KarFarma(BaseKarbaran):
    pass


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=model_image_directory_path)
