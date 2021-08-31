from django.contrib import admin

from .models import CourseCategory, Course

admin.site.register(CourseCategory)
admin.site.register(Course)