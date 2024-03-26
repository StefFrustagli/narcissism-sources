from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = CollaborateForm(
            {
            "name": "Paul", 
            "email": "test@test.com", 
            "message": "Hello!"
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        # test for 'name' field
        form = CollaborateForm({
            "name": "",
            "email":"test@test.com",
            "message": "Hi!"
        })
        # Use assert to determine if form is valid
        self.assertFalse(
            form.is_valid(), 
            msg="Name was not provided, but the form is valid"
            )

    def test_email_is_required(self):
        # test for 'email' field
        form = CollaborateForm({
            "name": "Soph",
            "email": "", 
            "message": "Hi!"
            })
        # Use assert to determine if form is valid
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        # test for 'message' field
        form = CollaborateForm({
            "name": "Soph", 
            "email": "test@test.com", 
            "message": ""
            })
        # Use assert to determine if form is valid
        self.assertFalse(
            form.is_valid(), 
            msg="Message was not provided, but the form is valid"
        )
