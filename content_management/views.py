from django.shortcuts import render, get_object_or_404
from .models import Content
from homepage.models import Topic


# Create your views here.
def resource_detail(request, topic_id):
    """
    Render the detail page for a specific topic's resources.

    Args:
        request (HttpRequest): The HTTP request object.
        topic_id (int): The ID of the topic
        whose resources are to be displayed.

    Returns:
        HttpResponse: The rendered HTML response displaying
        the topic's resources.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    content_set = Content.objects.filter(topic=topic)
    template = 'topic_detail.html'

    context = {
        'topic': topic,  # 'resource_detail' renamed to 'topic'
        'content_set': content_set
    }

    return render(
        request, template, context
    )
