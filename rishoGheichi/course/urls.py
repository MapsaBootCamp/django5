from django.urls import path

from .views import course_list, course_index, course_detail
urlpatterns = [
    path('', course_index, name='course_index'),
    path('course-list/', course_list, name='course_list'),
    path('course-detail/<int:id>', course_detail, name='course_detail'),
]
