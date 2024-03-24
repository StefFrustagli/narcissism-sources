from . import views
from django.urls import path

urlpatterns = [
    path("", views.TopicList.as_view(), name="home"),
    path("<slug:slug>/", views.topic_detail, name="topic_detail"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "<slug:slug>/content_list/",  # URL pattern for ContentList view
        views.ContentList.as_view(),  # Using the ContentList view
        name="content_list",  # Name for the URL pattern
    ),
]
