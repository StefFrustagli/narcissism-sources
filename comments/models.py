from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter", default=1)
    # body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ["created_on"]

    # def __str__(self):
    #     return f"Comment {self.body} by {self.author}"