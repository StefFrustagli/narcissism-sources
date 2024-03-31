from django.contrib import admin
from .models import Content
from comments.models import Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin):
    """
    Custom administration interface for Content model.

    This class provides an enhanced administration interface for managing
    Content objects in the Django admin site.

    Attributes:
        list_display (tuple): Specifies fields to display
        in the content list view.
        search_fields (list): Specifies fields to enable searching
        in the content list view.
        prepopulated_fields (dict): Specifies the fields whose values
        are automatically populated based on other fields.
        summernote_fields (tuple): Specifies the fields to enable Summernote
        rich text editor.
        list_filter (list): Specifies the fields to enable filtering
        in the content list view.
    """
    list_display = ("title", "slug", "topic")
    search_fields = ["title", "topic"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    list_filter = ["topic"]
