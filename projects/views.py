from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from projects.forms import ProjectForm

@login_required
def list_projects(request):
    item = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": item,
    }

    return render(request,"projects/list.html", context)

@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id, owner=request.user)
    context = {
        "project": project,
    }

    return render(request, "projects/detail.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
