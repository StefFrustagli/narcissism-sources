from . import views
from django.urls import path

urlpatterns = [
    path("<slug:slug>/", views.resource_detail, name="resource_detail"),
]
