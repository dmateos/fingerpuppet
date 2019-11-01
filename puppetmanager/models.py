import yaml
from django.db import models


class Configuration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    data = models.TextField()

    def bake_to_file(self, path: str):
        with open(path, "w+") as f:
            f.write(self.data)


class Classification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    configurations = models.ManyToManyField(Configuration)


class Node(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    classifications = models.ManyToManyField(Classification)

    def external_classify(self):
        base_data = {"classes": {}, "parameters": {}, "environment": "production"}

        for classification in self.classifications.all():
            for config in classification.configurations.all():
                base_data["classes"][config.name] = {}

        return yaml.dump(base_data, default_flow_style=False, explicit_start=True)
