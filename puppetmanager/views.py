from django.views.generic import ListView

from .models import Node, Classification, Configuration


class NodeList(ListView):
    template_name = "node/list.html"
    queryset = Node.objects.all()


class ClassificationList(ListView):
    template_name = "classification/list.html"
    queryset = Classification.objects.all()


class ConfigurationList(ListView):
    template_name = "configuration/list.html"
    queryset = Configuration.objects.all()
