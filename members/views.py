from django.template import RequestContext
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from projects.models import UserProjects

def index(request):

    try:
        avatar_url = settings.DEFAULT_AVATAR_URL

        project_list = UserProjects.objects.filter(user=request.user).order_by('start_date')

        return render_to_response('members/index.html',context_instance =
        RequestContext(request,{"default_avatar_url":avatar_url,
                                "project_list":project_list},
        ))

    except KeyError:
        #if the user isn't logged in a Key Error throws, so we'll dodge all of that and present a generic home page.
        return render_to_response('members/index.html',context_instance = RequestContext(request, {} ))

