from django.test import TestCase  # Import Django's testing library
from .forms import CommentForm # Import comment form to test


class TestCommentForm(TestCase):

    def test_form_is_valid(self): # Define function
        # Create an instance and fill out the body field with a string
        comment_form = CommentForm({"body": "This is a great post"}) 
        # Use assert to determine if form is valid
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')

    def test_form_is_invalid(self): 
        # Create an instance and fill out the body field with a string
        comment_form = CommentForm({"body": ""}) 
        # Use assert to determine if form is valid
        self.assertFalse(comment_form.is_valid(), msg='Form is valid')