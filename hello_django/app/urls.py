from django.urls import path

from .views import list_authors

urlpatterns = [
    path('authors/', list_authors),
]
