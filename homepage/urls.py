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
]
