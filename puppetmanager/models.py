from django.db import models


class Configuration(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)
    data = models.TextField()


class Classification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)

    configurations = models.ManyToManyField(Configuration)


class Node(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, null=False)

    classifications = models.ManyToManyField(Configuration)

    def external_classify(self):
        base_data = {"classes": {}, "parameters": {}, "environment": "production"}

        return base_data
