from django.contrib import admin

from . import models

admin.site.register(models.Author)
admin.site.register(models.ArticleCategory)
admin.site.register(models.Article)
admin.site.register(models.Chapter)
admin.site.register(models.Comment)
