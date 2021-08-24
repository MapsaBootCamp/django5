from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("self", null=True, blank=True,related_name="child_cat", on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Course(models.Model):
    pass