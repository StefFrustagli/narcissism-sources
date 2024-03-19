from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Topic
from comments.models import Comment
from .forms import CommentForm


# Create your views here.
class TopicList(generic.ListView):
    """
    View for displaying a list of topics.

    Attributes:
        queryset (QuerySet): The queryset containing all topics.
        template_name (str): The name of the template to render.
        paginate_by (int): The number of topics to display per page.
    """
    queryset = Topic.objects.all()
    template_name = "homepage/index.html"
    paginate_by = 6

def topic_detail(request, slug):
    """
    Display an individual topic with its comments.

    Context:
        topic (Topic): An instance of Topic.
        comments (QuerySet): All comments related to the topic.
        comment_count (int): The total count of comments for the topic.
        comment_form (CommentForm): The form for submitting new comments.

    Template:
        homepage/topic_detail.html
    """
    queryset = Topic.objects.filter(status=1)
    topic = get_object_or_404(queryset, slug=slug)
    comments = topic.comments.all().order_by("-created_on")
    comment_count = topic.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Comment submitted and awaiting approval"
            )

    comment_form = CommentForm()

    return render(
        request,
        "homepage/topic_detail.html",
        {
            "topic": topic,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit comments.

    If the form is valid and the comment belongs to the logged-in user,
    it updates the comment and displays a success message.
    Otherwise, it displays an error message.

    Redirects to the topic detail page after processing.
    """
    if request.method == "POST":

        queryset = Topic.objects.filter(status=1)
        topic = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.topic = topic
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("topic_detail", args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete comments.

    If the comment belongs to the logged-in user, it deletes the comment
    and displays a success message. Otherwise, it displays an error message.

    Redirects to the topic detail page after processing.
    """
    queryset = Topic.objects.filter(status=1)
    topic = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("topic_detail", args=[slug]))
