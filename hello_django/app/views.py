from django.shortcuts import render
from django.http import JsonResponse

from .models import Author, Article


def list_authors(request):
    authors_qs = Author.objects.all()

    authors_list = []
    for author in authors_qs:
        authors_list.append(
            {
                "name": author.name,
                "email": author.email
            }
        )
    return JsonResponse(authors_list, safe=False)

def show_articles(request):
    articles_list = list(Article.objects.filter(status=True).values("title", "body", "author__name","created_time"))
    # articles_qs = Article.objects.filter(status=True)
    # articles_list = []
    # for article in articles_qs:
    #     articles_list.append(
    #         {
    #             "title": article.title,
    #             "body": article.body,
    #             "created_time": article.created_time,
    #             "author": article.author.name
    #         }
    #     )

    return JsonResponse(articles_list, safe=False)

