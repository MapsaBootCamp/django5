from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

from users.models import Mentor


class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey("self", null=True, blank=True, related_name="child_cat", on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Course(models.Model):
    COURSE_STATUS = (
        ('d', 'deprecated'),
        ('f', 'finished'),
        ('i', 'inprogress')
    )
    title = models.CharField(_("عنوان دوره"), max_length=255)
    mentor = models.ForeignKey(Mentor, verbose_name=_("مدرس دوره"), on_delete=models.CASCADE)
    category = models.ForeignKey(CourseCategory, verbose_name=_("کتگوری درس"), null=True,
                                 related_name="course_category", on_delete=models.SET_NULL)
    status = models.CharField(_("وضعیت"), max_length=1, choices=COURSE_STATUS)
    description = models.TextField()
    commentable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class CourseChapter(models.Model):
    course = models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.chapter_title}"


class CourseComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_time = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name = 'comments', on_delete=models.CASCADE)
    rate = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return f"{self.user.email}-{self.comment[:20]}"