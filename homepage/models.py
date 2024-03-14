from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    # page_url = models.URLField()  # Add this field to store the URL of the page
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Topic: {self.title}"
