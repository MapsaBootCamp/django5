from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


from .models import Author


@receiver(post_save, sender=User)
def create_authors(sender, instance, created, **kwargs):
    if created:
        try:
            Author.objects.create(user=instance)

        except:
            instance.delete()


# post_save.connect(create_authors, sender=User)
