from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """
        Test case class for validating the CollaborateForm form.

        This class contains test methods to validate the behavior
        of the CollaborateForm form under various scenarios,
        including valid data input and required field validation.

        Test methods:
            - test_form_is_valid: Test for all fields with valid data input.
            - test_name_is_required: Test for required 'name' field
              with empty input.
            - test_email_is_required: Test for required 'email' field
              with empty input.
            - test_message_is_required: Test for required 'message' field
              with empty input.
        """
        form = CollaborateForm(
            {"name": "Paul", "email": "test@test.com", "message": "Hello!"}
        )
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        # test for 'name' field
        form = CollaborateForm(
            {
                "name": "",
                "email": "test@test.com",
                "message": "Hi!"
            })
        # Use assert to determine if form is valid
        self.assertFalse(
            form.is_valid(), msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        # test for 'email' field
        form = CollaborateForm({"name": "Soph", "email": "", "message": "Hi!"})
        # Use assert to determine if form is valid
        self.assertFalse(
            form.is_valid(), msg="Email was not provided, but form is valid"
        )

    def test_message_is_required(self):
        # test for 'message' field
        form = CollaborateForm(
            {"name": "Soph", "email": "test@test.com", "message": ""}
        )
        # Use assert to determine if form is valid
        self.assertFalse(
            form.is_valid(), msg="Message was not provided, but form is valid"
        )
