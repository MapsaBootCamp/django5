from django.urls import path

from .views import AuthorList, AuthorDetail, ArticleListView, ArticleDetailView, CommentView

urlpatterns = [
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>', ArticleDetailView.as_view()),
    path('comment/', CommentView.as_view()),
    path('comment/<int:pk>', CommentView.as_view()),
]
