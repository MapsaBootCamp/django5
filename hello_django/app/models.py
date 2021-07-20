from django.db import models


class Author(models.Model):
    """
    تیبلی در دیتابیس خواهیم داشت که فیلدهای این کلاس ستونهای تیبل آن هستند

    """
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
