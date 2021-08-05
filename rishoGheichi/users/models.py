from django.db import models
from django.contrib.auth import get_user_model
from utils.models_utils import model_image_directory_path

User = get_user_model()


class Karjoo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=model_image_directory_path)


    @property
    def karjoo_name(self):
        return
