from django.template import RequestContext
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from projects.models import UserProjects, UserProjectsForm

@login_required
def project_detail(request, proj_id):

    project = get_object_or_404(UserProjects,pk=proj_id)

    #so only staff users and the users themselves can see a given project page.
    if ((request.user.username == project.user.username) or (request.user.is_staff)):
        return render_to_response('projects/detail.html',context_instance = RequestContext(request,{"project":project,}))
    else:
        redir_url = "/members/profiles/%s" % project.user.username
        return HttpResponseRedirect(redir_url)

@login_required
def project_delete(request, proj_id):

    project = get_object_or_404(UserProjects,pk=proj_id)

    if ((request.user.username == project.user.username) or (request.user.is_superuser)):
        project.delete()
        return render_to_response('projects/delete.html',context_instance = RequestContext(request,{}))
    else:
        return render_to_response('projects/no_delete.html',context_instance = RequestContext(request,{}))

@login_required
def project_create(request):
    if request.method == 'POST':
        form = UserProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/saved/')
    else:
        form = UserProjectsForm(initial={'user':request.user})

    return render_to_response('projects/edit.html',context_instance = RequestContext(request,{'form':form}))

@login_required
def project_edit(request, proj_id):
    instance = get_object_or_404(UserProjects, pk=proj_id)
    form = UserProjectsForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/projects/saved/')

    return render_to_response('projects/edit.html',context_instance = RequestContext(request,{'form':form}))

@login_required
def project_saved(request):

    return render_to_response('projects/saved.html',context_instance = RequestContext(request,{}))
