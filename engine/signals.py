from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Account

@receiver(post_save, sender=User, dispatch_uid="user_account_set")
def user_account_set(sender, instance, **kwargs):
    if not instance.account_set.first():
        account = Account.objects.create(name=instance.username, user=instance)
