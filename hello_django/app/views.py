from django.shortcuts import render
from django.http import JsonResponse

from .models import Author


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

def show_article(request):
    pass
