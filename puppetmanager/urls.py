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
        "classifications/delete/<int:pk>",
        views.ClassificationDelete.as_view(),
        name="classification_delete",
    ),
    path(
        "configurations", views.ConfigurationList.as_view(), name="configuration_list"
    ),
    path(
        "configurations/new",
        views.ConfigurationCreate.as_view(),
        name="configuration_create",
    ),
    path(
        "configurations/edit/<int:pk>",
        views.ConfigurationUpdate.as_view(),
        name="configuration_update",
    ),
    path(
        "configurations/delete/<int:pk>",
        views.ConfigurationDelete.as_view(),
        name="configuration_delete",
    ),
]
