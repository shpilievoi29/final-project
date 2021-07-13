from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.conf import settings
from user.models import Cash


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        Cash.objects.create(username_id=instance.id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
