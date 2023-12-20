from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)

@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "show_my_tasks" : tasks,
    }
    return render (request, "tasks/mine.html", context)
