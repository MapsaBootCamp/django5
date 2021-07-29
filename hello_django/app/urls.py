from django.urls import path

from .views import list_authors, show_articles, edit_article

urlpatterns = [
    path('authors/', list_authors),
    path('articles/', show_articles),
    path('edit-article/<int:id>', edit_article),


]
