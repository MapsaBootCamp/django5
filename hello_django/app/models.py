from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """
    تیبلی در دیتابیس خواهیم داشت که فیلدهای این کلاس ستونهای تیبل آن هستند

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name="نام", max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    تیبل مقالاتی که حضرات نویسنده علیه سلام زحمت کشیدند نوشتند
    """
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# article---> title --> charfield 255, body ---> textfielf, author(ye juroi baiad be author vasl she), created time ---> datetimefiled(auto_now_add=true), status booleanfield(default=True)
# comment ---> name---> charfield, text---> textfield, article( hamun )


class Comment(models.Model):
    """
    commnet fields: commenter, body, article
    """
    RATE_CHOICE = (
        ("p", "positive"),
        ("n", "negative")
    )

    name = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    rate = models.CharField(max_length=1, null=True,
                            blank=True, choices=RATE_CHOICE)

    def __str__(self):
        return f"{self.name} - {self.body[:20]} -{self.article.title}"
