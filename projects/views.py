from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

@login_required
def list_projects(request):
    item = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": item,
    }

    return render(request,"projects/list.html", context)
