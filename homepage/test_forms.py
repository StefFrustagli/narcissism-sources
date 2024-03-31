from django.test import TestCase  # Import Django's testing library
from .forms import CommentForm  # Import comment form to test


class TestCommentForm(TestCase):
    """
    Test case class for testing the CommentForm.

    This class contains test methods to verify the behavior of the CommentForm,
    including form validation for valid and invalid inputs.

    Test methods:
        - test_form_is_valid: Test form validation with valid input.
        - test_form_is_invalid: Test form validation with invalid input.
    """
    def test_form_is_valid(self):  # Define function
        """
        Test method to verify form validation with valid input.

        This method creates an instance of the CommentForm and fills out the
        body field with a valid string. It then checks if the form is valid.
        """
        # Create an instance and fill out the body field with a string
        comment_form = CommentForm({"body": "This is a great post"})
        # Use assert to determine if form is valid
        self.assertTrue(comment_form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid(self):
        """
        Test method to verify form validation with invalid input.

        This method creates an instance of the CommentForm and fills out the
        body field with an empty string. It then checks if the form is invalid.
        """
        # Create an instance and fill out the body field with a string
        comment_form = CommentForm({"body": ""})
        # Use assert to determine if form is valid
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
