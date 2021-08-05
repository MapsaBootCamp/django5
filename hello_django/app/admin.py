from django.contrib import admin

from .models import Author, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ["update_time"]


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
