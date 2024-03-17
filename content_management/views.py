from django.shortcuts import render, get_object_or_404
from .models import Content
from homepage.models import Topic


# Create your views here.
def resource_detail(request, topic_id):
    """

    """
    resource_detail = get_object_or_404(Topic, id= topic_id)
    content_set = Content.objects.filter(topic=topic)

    # content_set = Content.objects.filter(content=content)

    template = 'resource_detail.html'

    context = {
        'resource_detail': resource_detail,
        'content_set': content_set
    }

    return render(
        request, template, context
    )
