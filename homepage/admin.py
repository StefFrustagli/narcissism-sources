from django.contrib import admin
from .models import Topic
from django_summernote.admin import SummernoteModelAdmin


# Admin panel functionality
@admin.register(Topic)
class PostAdmin(SummernoteModelAdmin):
    """
    Custom admin panel configuration for the 'Topic' model.

    This class configures the admin panel functionality for the 'Topic' model.
    It specifies how the Topic model should be displayed and managed in the
    Django admin interface.

    Attributes:
        list_display (tuple): Specifies the fields to display in the list view
        of the admin panel (title, slug, status, created_on).
        search_fields (list): Specifies the fields to search for when using the
        search bar in the admin panel (title, content).
        list_filter (tuple): Specifies the fields to use as filters in the
        sidebar of the admin panel (status).
        prepopulated_fields (dict): Specifies fields whose values are
        automatically generated based on other fields (slug based on title).
        summernote_fields (tuple): Specifies the fields to be enhanced with
        Summernote WYSIWYG editor in the admin panel (content).
    """

    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


# Register your models here.
