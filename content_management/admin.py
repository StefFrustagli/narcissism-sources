from django.contrib import admin
from .models import Content
from comments.models import Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug", "topic")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)



# Register your models here.
