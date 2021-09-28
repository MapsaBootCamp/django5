from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.SmallIntegerField(null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(
        Author, related_name="articles", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ArticleCategory, related_name='articles', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    article = models.ForeignKey(
        Article, related_name='chapters', on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=255)
    chapter_number = models.SmallIntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article.title}-{self.chapter_number}"


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name = "comments" ,on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.user
