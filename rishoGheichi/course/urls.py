from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import course_list, course_index, course_detail, test_celery
from course.api.api_views import CourseViewSet


router = SimpleRouter()

router.register("course", CourseViewSet, basename="course")


urlpatterns = [
    path('', course_index, name='course_index'),
    path('course-list/', course_list, name='course_list'),
    path('course-detail/<int:id>', course_detail, name='course_detail'),
    path("api/", include(router.urls)),
    path('async-sum/', test_celery)
]
