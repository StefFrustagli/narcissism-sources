from django.shortcuts import render
from django.views import generic
from .models import Topic


# Create your views here.
class TopicList(generic.ListView):
    queryset = Topic.objects.all()
    template_name = "homepage/index.html"
    paginate_by = 6
