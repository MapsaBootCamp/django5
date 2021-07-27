from django.urls import path

from .views import list_authors, show_articles

urlpatterns = [
    path('authors/', list_authors),
    path('articles/', show_articles),

]
