from django.db import models
from django.contrib.auth.models import User
from content_management.models import Content
from content_management.models import Source
from django.contrib.auth import get_user_model

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", default=1
    )
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE, related_name="comments", blank=True
    )
    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
        related_name="comments",
        default=None,
        blank=True,
    )
    body = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ["created_on"]

    # def __str__(self):
    #     return f"Comment {self.body} by {self.author}"
