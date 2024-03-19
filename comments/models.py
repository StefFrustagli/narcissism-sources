from django.db import models
from django.contrib.auth.models import User
from content_management.models import Content, Topic
from django.contrib.auth import get_user_model

# This model represents comments on topics.
# It is part of the "comments" app, which will be expanded to include
# community features in the future.
class Comment(models.Model):
    """
    Represents a comment made by a user on a topic.

    Attributes:
        author (User): The user who made the comment.
        topic (Topic): The topic on which the comment was made.
        body (str): The content of the comment.
        created_on (DateTime): The date/time when the comment was created.
        updated_on (DateTime): The date/time when the comment was last updated.
        approved (bool): Indicates whether the comment has been approved.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", default=1
    )
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="comments", default=1
    )
    body = models.TextField(default="")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
