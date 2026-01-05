from django.shortcuts import render, redirect
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request, "home.html")


def todos(request):
    if request.method == "POST":
        new_todo = request.POST.get("new_todo")
        TodoItem.objects.create(title=new_todo)
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


def toggle_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("/todos")


def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect("/todos")
