from django.contrib import admin

from .models import CourseCategory, Course, CourseChapter, CourseComments

admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(CourseChapter)
admin.site.register(CourseComments)