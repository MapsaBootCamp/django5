import json

from django.core.serializers import serialize
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

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
    articles_list = list(
        Article.objects.filter(status=True).values("id", "title", "body", "author__name", "created_time"))
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


@csrf_exempt
@require_http_methods(["POST"])
def create_article(request):
    data = json.loads(request.body)
    author = data.get("author", None)
    title = data.get("title", None)
    body = data.get("body", None)
    if author and title and body:
        authors = Author.objects.filter(name=author)
        if authors:
            article_obj = Article(title=data.get("title"), body=data.get("body"), author=authors[0])
            article_obj.save()
            return JsonResponse({"status":"201"})
        else:
            raise PermissionDenied
    else:
        return JsonResponse({"error": "field author ya title ya body peida nashod"})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    author_is_user = json.loads(request.body).get("author", None) == article.author.name

    if author_is_user:
        try:
            article.delete()
            return JsonResponse({"status": "204"})
        except IntegrityError as e:
            return JsonResponse({"error": str(e)})
    else:
        raise PermissionDenied

@require_http_methods(["POST"])
@csrf_exempt
def create_comment(request, article_id):
    pass