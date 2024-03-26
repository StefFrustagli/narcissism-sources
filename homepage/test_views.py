from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from .forms import CommentForm
from .models import Topic


class TestHomepageViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername", 
            password="myPassword", 
            email="test@test.com"
        )
        current_datetime = timezone.now()  # Define current datetime
        self.topic = Topic(
            title="Media",
            slug="media",
            description="",
            custom_order=2,
            status=1,
            created_on=current_datetime,
        )

    def test_render_topic_detail_page(self):
        response = self.client.get(reverse("topic_detail", args=["media"]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Media", response.content)
        self.assertIsInstance(response.context["comment_form"], CommentForm)
