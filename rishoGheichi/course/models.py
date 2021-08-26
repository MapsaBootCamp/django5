from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Mentor


class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("self", null=True, blank=True,related_name="child_cat", on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Course(models.Model):
    COURSE_STATUS = (
        ('d', 'deprecated'),
        ('f', 'finished'),
        ('i', 'inprogress')
    )
    title = models.CharField(_("عنوان دوره"), max_length=255)
    mentor = models.ForeignKey(Mentor, verbose_name = _("مدرس دوره") , on_delete=models.CASCADE)
    category = models.ForeignKey(CourseCategory, verbose_name=_("کتگوری درس"), null=True, related_name= "course_category", on_delete=models.SET_NULL)
    status = models.CharField(_("وضعیت"), max_length=1, choices=COURSE_STATUS)
    description = models.TextField()


class CourseChapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=300)


class CourseComments(models.Model):
    pass