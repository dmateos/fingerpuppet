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
        "classifications/new",
        views.ClassificationCreate.as_view(),
        name="classification_create",
    ),
    path(
        "classifications/edit/<int:pk>",
        views.ClassificationUpdate.as_view(),
        name="classification_update",
    ),
    path(
        "configurations", views.ConfigurationList.as_view(), name="configuration_list"
    ),
]
