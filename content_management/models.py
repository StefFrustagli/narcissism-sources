from django.db import models
from django.contrib.auth.models import User
from homepage.models import Topic

class Content(models.Model):
    """
    Represents content associated with a topic.

    Attributes:
        topic (Topic): The topic to which the content belongs.
        title (str): The title of the content.
        slug (str): A unique slug for the content.
        source (str): The source of the content (e.g., Instagram or YouTube).
        source_identifier (str): The unique identifier for the content.
        description (str): A description of the content.
        embed_code (str): The embed code for displaying the content.
    """
    CONTENT_SOURCES = (
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
    )
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="content_set")
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    source = models.CharField(max_length=25, choices=CONTENT_SOURCES)
    # This is the unique identifier for the video on YT/Instagram
    source_identifier = models.CharField(max_length=25, default='0')
    description = models.TextField()
    embed_code = models.TextField()  # Store the embed code for the Instagram reel
