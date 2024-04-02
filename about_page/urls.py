from . import views
from django.urls import path

urlpatterns = [
    # Mapping the root URL (empty string) to the about_page view function
    path("", views.about_page, name="about_page"),
]
