from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from .models import CourseCategory, Course
from .tasks import summation



def course_index(request):
    course_cat_objects_qs = CourseCategory.objects.all()

    context = {
        "course_cat_objects": course_cat_objects_qs,
        "date": datetime.strptime("26/08/2021", "%d/%m/%Y")
    }
    return render(request, "course/index.html", context)



# list all course
@cache_page(60 * 60, cache="sholagh")
# @vary_on_cookie
def course_list(request):
    if request.method == "GET":
        title_filter = request.GET.get('title', None)
        mentor_filter = request.GET.get('mentor', None)
        course_cat_objects_qs = CourseCategory.objects.select_related('category').all()
        courses_qs = Course.objects.all()
        if title_filter:
            courses_qs = courses_qs.filter(title__contains=title_filter)
        if mentor_filter:
            print("hello")
            courses_qs = courses_qs.filter(mentor__user__email__contains=mentor_filter)
        session_cart = request.session.get("cart", [])
        if not cache.get("counter"):
            cache.set("counter", 0)
        counter = cache.get("counter") + 1
        cache.set("counter", counter)
        context = {
            "course_cat_objects": course_cat_objects_qs,
            'courses': courses_qs,
            'title': "لیست دوره ها",
            "cart": session_cart,
            "counter" : counter
        }
        print(cache.get("name"))
        return render(request, 'course/course_list.html', context)


# course detail
@require_http_methods(["GET"])
def course_detail(request, id):
    course_obj = get_object_or_404(Course, id=id)
    session_cart = request.session.get("cart", [])
    context = {
        "cart": session_cart,
        "title": course_obj.title,
        "course": course_obj,
        "comments": course_obj.comments.select_related("user").all()
    }
    return render(request, 'course/course_detail.html', context)


def test_celery(request):

    summation.delay(5, 5)

    return HttpResponse("ba celery anjam shod")