from django.db import models
from django.contrib.auth.models import User


class AppConfiguration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    some_config_option = models.TextField(default="")

    class Meta:
        get_latest_by = "created"

    @staticmethod
    def get(name):
        config = AppConfiguration.objects.latest()
        return getattr(config, name)


class Account(models.Model):
    """
    This is an account that will be linked to a django user
    """

    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
