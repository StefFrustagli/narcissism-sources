from . import views
from django.urls import path

urlpatterns = [
    # URL pattern for the homepage
    path("", views.TopicList.as_view(), name="home"),
    # URL pattern for displaying topic details
    path("<slug:slug>/", views.topic_detail, name="topic_detail"),
    # URL pattern for editing comments
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    # URL pattern for deleting comments
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    # URL pattern for listing content related to a topic
    path(
        "<slug:slug>/content_list/",  # URL pattern for ContentList view
        views.ContentList.as_view(),  # Using the ContentList view
        name="content_list",  # Name for the URL pattern
    ),
]
