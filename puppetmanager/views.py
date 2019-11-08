from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Node, Classification, Configuration


class NodeList(ListView):
    template_name = "node/list.html"
    queryset = Node.objects.all()


class ClassificationList(ListView):
    template_name = "classification/list.html"
    queryset = Classification.objects.all()


class ClassificationCreate(CreateView):
    model = Classification
    template_name = "classification/classification_form.html"
    success_url = reverse_lazy("classification_list")
    fields = ["name"]


class ClassificationUpdate(UpdateView):
    model = Classification
    template_name = "classification/classification_form.html"
    success_url = reverse_lazy("classification_list")
    fields = ["name"]


class ConfigurationList(ListView):
    template_name = "configuration/list.html"
    queryset = Configuration.objects.all()


class ConfigurationCreate(CreateView):
    model = Configuration
    template_name = "configuration/configuration_form.html"
    success_url = reverse_lazy("configuration_list")
    fields = ["name", "data"]


class ConfigurationUpdate(UpdateView):
    model = Configuration
    template_name = "configuration/configuration_form.html"
    success_url = reverse_lazy("configuration_list")
    fields = ["name", "data"]
