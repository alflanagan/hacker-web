"""Views related to / used by members (not admin)."""
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from projects.models import UserProjects

def index(request):
    """Basic member view, showing avatar and projects."""
    if request.user.is_authenticated():
        avatar_url = settings.DEFAULT_AVATAR_URL
        project_list = UserProjects.objects.filter(user=request.user).order_by('start_date')

        return render_to_response('members/index.html',
                                  context=RequestContext(request,
                                                         {"default_avatar_url": avatar_url,
                                                          "project_list": project_list}))
    else:
        return render_to_response('members/index.html', {})
