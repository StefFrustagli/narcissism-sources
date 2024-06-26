"""
URL configuration for narcissism_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500, handler403, handler405

# URL patterns list
urlpatterns = [
    path("about_page/", include("about_page.urls"), name="about_page-urls"),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("comments/", include("comments.urls")),
    path("content_management/", include("content_management.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("", include("homepage.urls"), name="homepage-urls"),
]

# Handling custom error pages
handler404 = "narcissism_website.views.handler404"
handler500 = "narcissism_website.views.handler500"
handler403 = "narcissism_website.views.handler403"
handler405 = "narcissism_website.views.handler405"
