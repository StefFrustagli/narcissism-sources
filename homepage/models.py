from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Topic(models.Model):
    """
    Model representing a topic.

    Attributes:
        title (str): The title of the topic.
        slug (str): The slug for the topic.
        featured_image (CloudinaryField): The featured image of the topic.
        description (str): The description of the topic.
        custom_order (int): The custom order for sorting topics.
        status (int): The status of the topic (Draft or Published).
        created_on (datetime): The date and time when the topic was created.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    custom_order = models.IntegerField(default=0)  # Field for custom ordering
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["custom_order"]

    def __str__(self):
        return f"Topic: {self.title}"
