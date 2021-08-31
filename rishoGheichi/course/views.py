from datetime import datetime
from django.shortcuts import render

from .models import CourseCategory, Course


def course_index(request):
    course_cat_objects_qs = CourseCategory.objects.all()

    context = {
        "course_cat_objects": course_cat_objects_qs,
        "date": datetime.strptime("26/08/2021", "%d/%m/%Y")
    }
    return render(request, "course/index.html", context)


# list all course
def course_list(request):
    if request.method == "GET":
        course_cat_objects_qs = CourseCategory.objects.all()
        courses_qs = Course.objects.all()
        print(courses_qs)
        context = {
            "course_cat_objects": course_cat_objects_qs,
            'courses': courses_qs,
            'title': "لیست دوره ها"
        }
        return render(request, 'course/course_list.html', context)


# course detail
def course_detail(request, id):
    pass