from django.urls import path

from .views import course_index
urlpatterns = [
    path('', course_index, name='course_index')
]
