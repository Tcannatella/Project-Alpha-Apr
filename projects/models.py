from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=200)
    description	 = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "projects",
        on_delete=models.CASCADE,
        null=True,


    )
    def __str__(self):
        return self.name

def create_project(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.id)
    else:
        form = TodoItemForm()

    context = {
        "form": form,
    }
    return render(request,"todos/itemscreate.html", context)
