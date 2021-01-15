from django.db.models.signals import post_save
from django.dispatch import receiver
from TestApp.tasks import send_rating
from TestApp.models import Rating


@receiver(post_save, sender=Rating)
def rating(sender, instance, **kwargs):
    if instance== True:
        send_rating.apply_async(eta=now)
                                  