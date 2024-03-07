from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_comment(request):
    return HttpResponse("Hello, I'm a comment!")
