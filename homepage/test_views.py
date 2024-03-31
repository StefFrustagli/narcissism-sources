from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from .forms import CommentForm
from .models import Topic


class TestHomepageViews(TestCase):
    """
    Test case class for testing views related to the homepage.

    This class contains test methods to verify the behavior of views
    associated with the homepage, including topic creation and rendering
    the topic detail page.

    Test methods:
        - test_topic_created: Check if the topic is created successfully.
        - test_render_topic_detail_page: Test rendering
        of the topic detail page.
    """
    def setUp(self):
        """
        Set up method to create necessary objects for testing.

        This method creates a superuser, a topic, and other required objects
        before executing each test method.
        """
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        current_datetime = timezone.now()  # Define current datetime
        self.topic = Topic.objects.create(
            title="Other media",
            slug="other-media",
            description="",
            custom_order=2,
            status=1,
            created_on=current_datetime,
        )

    # Check if the topic exists
    def test_topic_created(self):
        """
        Test method to verify the creation of a topic.

        This method checks if the topic with the specified slug is created
        successfully in the database.
        """
        topics = Topic.objects.filter(slug="other-media")
        self.assertEqual(len(topics), 1)

    def test_render_topic_detail_page(self):
        response = self.client.get(reverse(
            "topic_detail", args=["other-media"]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Other media", response.content)
        self.assertIsInstance(response.context["comment_form"], CommentForm)
