import yaml
import os
from django.db import models


class Configuration(models.Model):
    """
    Represents a puppet recipe.
    """

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    data = models.TextField()

    def __str__(self) -> str:
        return self.name

    def bake_to_file(self, path: str) -> None:
        config_path = "{}/{}/manifests".format(path, self.name)
        if not os.path.exists(config_path):
            os.makedirs(config_path)

        with open("{}/init.pp".format(config_path), "w+") as f:
            f.write(self.data)

    def restart_puppet(self):
        return False


class Classification(models.Model):
    """
    Classifications are used to classify a node as a certain type of "thing".
    These hold many configurations that will be applied to a node.
    """

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    configurations = models.ManyToManyField(Configuration)

    def __str__(self) -> str:
        return self.name


class Node(models.Model):
    """
    Nodes represent a single physical entity managed by puppet.
    """

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    classifications = models.ManyToManyField(Classification, blank=True)
    total_checkins = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    def external_classify(self) -> str:
        base_data = {"classes": {}, "parameters": {}, "environment": "production"}

        for classification in self.classifications.all():
            for config in classification.configurations.all():
                base_data["classes"][config.name] = {}

        return yaml.dump(base_data, default_flow_style=False, explicit_start=True)

    def update(self) -> None:
        self.total_checkins += 1
        self.save()
