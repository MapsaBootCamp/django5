from django.urls import path

from .views import list_authors, show_articles, edit_article, delete_article, create_article, create_comment, \
    show_all_comment

urlpatterns = [
    path('authors/', list_authors, name="authors"),
    path('articles/', show_articles, name="articles"),
    path('edit-article/<int:id>', edit_article),
    path('delete-article/<int:id>', delete_article),
    path('create-article/', create_article),
    path('create-comment/<int:article_id>', create_comment),
    path('show-comment/<int:article_id>', show_all_comment),
]
