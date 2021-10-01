from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_khodi = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        User, related_name="follower", through="Follow")

    def __str__(self):
        return self.user_khodi.username


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} follows {self.profile.user_khodi.username}"

    def save(self, *args, **kwargs):
        if self.profile.user_khodi.id == self.user.id:
            raise Exception("shab bekheir")

        return super().save(*args, **kwargs)
