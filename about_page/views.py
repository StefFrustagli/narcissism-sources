from django.shortcuts import render
from .models import About

# Create your views here.


def about_page(request):
    """
    Renders the About page
    """
    about_page = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about_page/about_page.html",
        {"about_page": about_page},
    )
