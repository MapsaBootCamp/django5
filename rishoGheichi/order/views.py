from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from course.models import Course
def course_add_to_cart(request, course_id):
    if not Course.objects.filter(id=course_id).exists():
        return HttpResponse("shalgham hackeri! boro bemir.")
    request.session["cart"] = request.session.get("cart", [])
    if course_id not in request.session["cart"]:
        request.session["cart"].append(course_id)
    request.session.set_expiry(30)
    return HttpResponse("dame shoma garm")

