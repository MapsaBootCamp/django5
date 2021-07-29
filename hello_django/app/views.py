import json

from django.core.serializers import serialize
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
    articles_list = list(Article.objects.filter(status=True).values("title", "body", "author__name", "created_time"))
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


@csrf_exempt
def edit_article(request, id):
    if request.method == "GET":
        article = Article.objects.filter(id=id).values().first()
        # article = get_object_or_404(Article, id=id)
        # result = {"title": article.title, "body": article.body, "author": article.author.name}
        # data = serialize("json", article, fields=('title', 'body', "author"))
        # return HttpResponse(data, content_type="application/json")

        return JsonResponse(article, safe=False)
        # try:
        #     article = Article.objects.get(id=id)
        #     result = {"title": article.title, "body": article.body, "author": article.author.name}
        #     return JsonResponse(result)
        # except ObjectDoesNotExist as e:
        #     return JsonResponse({"status": "not found", "error": str(e)})
    elif request.method == "PUT":
        data = json.loads(request.body)
        article = get_object_or_404(Article, id=id)
        article.title = data.get("title", article.title)
        article.body = data.get("body", article.body)
        article.save()
        return JsonResponse({"status": "ba khubi va khosi update shod"})

    return JsonResponse({"status": "no ok", "error": "faghat get va put"})
