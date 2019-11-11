import os
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Configuration


@receiver(post_save, sender=Configuration, dispatch_uid="config_save_update_files")
def configuration_update(sender, instance, **kwargs):
    module_path = os.environ.get("PUPPET_MODULE_PATH", False)
    if module_path:
        instance.bake_to_file(module_path)
        instance.restart_puppet()
