from django.db import models


class Author(models.Model):
    """
    تیبلی در دیتابیس خواهیم داشت که فیلدهای این کلاس ستونهای تیبل آن هستند

    """
    name = models.CharField(verbose_name="نام",max_length=200)
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
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


### article---> title --> charfield 255, body ---> textfielf, author(ye juroi baiad be author vasl she), created time ---> datetimefiled(auto_now_add=true), status booleanfield(default=True)
### comment ---> name---> charfield, text---> textfield, article( hamun )