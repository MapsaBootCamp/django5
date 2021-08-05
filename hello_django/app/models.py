from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.constraints import UniqueConstraint
from django.utils.translation import gettext as _


class Author(models.Model):
    """
    تیبلی در دیتابیس خواهیم داشت که فیلدهای این کلاس ستونهای تیبل آن هستند

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name="نام", max_length=200)
    email = models.EmailField()

    class Meta:
        # unique_together = [['name', 'email']]
        UniqueConstraint(fields=['name', 'email'], name='unique_author')
        verbose_name = _("naneh ghamar")
        verbose_name_plural = _("naneh ghamars")

    @property
    def email_befor_domain(self):
        return self.email.split('@')[0]

    def __str__(self):
        return self.name


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

    def truncate(self):
        pass


class Article(models.Model):
    """
    تیبل مقالاتی که حضرات نویسنده علیه سلام زحمت کشیدند نوشتند
    """
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField()
    status = models.BooleanField(default=True)

    objects = models.Manager()
    objects_active = ArticleManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.update_time = timezone.now()
        if "boogh" in self.body:
            return
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
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


class BaseInheritance(models.Model):
    age = models.SmallIntegerField()

    class Meta:
        abstract = True


class DerivedA(BaseInheritance):
    pass


class DerivedB(BaseInheritance):
    name = models.CharField(max_length=255)
