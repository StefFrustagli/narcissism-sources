from django.db import models
from django.contrib.auth.models import User
from homepage.models import Topic

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    embed_code = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
