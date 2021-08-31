from django.urls import path, include

from .views import show_resume
urlpatterns = [
    path('', show_resume),
]
