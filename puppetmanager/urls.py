from django.urls import path
from . import views


urlpatterns = [
    path("nodes", views.NodeList.as_view(), name="node_list"),
    path(
        "classifications",
        views.ClassificationList.as_view(),
        name="classification_list",
    ),
    path(
        "configurations", views.ConfigurationList.as_view(), name="configuration_list"
    ),
]
