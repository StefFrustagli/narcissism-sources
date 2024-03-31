from comments.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class for creating and updating comments.

    This form is used to create and update comments.
    It specifies the fields to be included in the form and the model
    to which the form corresponds.

    Attributes:
        model (class): Specifies the model
        to which the form corresponds (Comment).
        fields (tuple): Specifies the fields to be included in the form
        (only 'body' field).
    """
    class Meta:
        model = Comment
        fields = ("body",)
