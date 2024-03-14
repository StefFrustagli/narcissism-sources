from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse


# Create your views here.
def my_comment(request):
    return HttpResponse("Hello, I'm a comment!")
