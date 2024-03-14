from django.db import models
from django.contrib.auth.models import User
from homepage.models import Topic

class Content(models.Model):
    CONTENT_SOURCES = (
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    source = models.CharField(max_length=25, choices=CONTENT_SOURCES)
    # This is the unique identifier for the video on YT/Instagram
    source_identifier = models.CharField(max_length=25, default='0')
    description = models.TextField()
    embed_code = models.TextField()  # Store the embed code for the Instagram reel