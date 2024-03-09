from django.contrib import admin
from .models import Source, Content
from comments.models import Comment
from .models import Content, Source
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Source)
class SourceAdmin(SummernoteModelAdmin):

    search_fields = ["title"]
    summernote_fields = ("content",)


# Register your models here.
