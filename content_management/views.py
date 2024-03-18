from django.shortcuts import render, get_object_or_404
from .models import Content
from homepage.models import Topic


# Create your views here.
def resource_detail(request, topic_id):
    """
    Display resource detail for a specific topic
    """
    topic = get_object_or_404(Topic, id= topic_id)
    content_set = Content.objects.filter(topic=topic)

    # content_set = Content.objects.filter(content=content)

    template = 'topic_detail.html'

    context = {
        'topic': topic, # 'resource_detail' renamed to 'topic'
        'content_set': content_set
    }

    return render(
        request, template, context
    )
