from django.shortcuts import render
from projects.models import Project

def list_projects(request):
    item = Project.objects.all()
    context = {
        "list_projects": item,
    }

    return render(request,"projects/list.html", context)
