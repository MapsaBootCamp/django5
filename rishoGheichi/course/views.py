from django.shortcuts import render

from .models import CourseCategory


def course_index(request):
    course_cat_objects_qs = CourseCategory.objects.all()
    context = {
        "course_cat_objects": course_cat_objects_qs
    }
    return render(request, "course/index.html", context)