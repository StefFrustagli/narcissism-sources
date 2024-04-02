from . import views
from django.urls import path

urlpatterns = [
    # Mapping URL pattern with slug parameter to resource_detail view function
    path("<slug:slug>/", views.resource_detail, name="resource_detail"),
]
