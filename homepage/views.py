from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Topic


# Create your views here.
class TopicList(generic.ListView):
    queryset = Topic.objects.all()
    template_name = "homepage/index.html"
    paginate_by = 6


def topic_detail(request, slug):
    """
    Display an individual :model:`homepage.Topic`.

    **Context**

    ``topic``
        An instance of :model:`homepage.Topic`.

    **Template:**

    :template:`homepage/topic_detail.html`
    """

    queryset = Topic.objects.filter(status=1)
    topic = get_object_or_404(queryset, slug=slug)
    comments = topic.comments.all().order_by("-created_on")
    comment_count = topic.comments.filter(approved=True).count()

    return render(
        request,
        "homepage/topic_detail.html",
        {
            "topic": topic,
            "comments": comments,
            "comment_count": comment_count,
        },
    )
