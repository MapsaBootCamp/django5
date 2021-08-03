from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("self", null=True, blank=True)

    def __str__(self):
        return self.name




class Course(models.Model):
    pass