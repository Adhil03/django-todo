from django.shortcuts import render, redirect
from .models import TodoItem


# Create your views here.
def home(request):
    return render(request, "home.html")


def todos(request):
    if request.method == "POST":
        new_todo = request.POST.get("new_todo")
        category = request.POST.get("category")
        TodoItem.objects.create(title=new_todo, category=category)
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


def about(request):
    return render(request, "about.html")


def contact(request):
    # Just list your accounts here
    social_accounts = [
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com/in/yourusername",
            "icon": "bi-linkedin",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/yourusername",
            "icon": "bi-github",
        },
        {
            "name": "Email",
            "url": "mailto:adlpro253@gmail.com",
            "icon": "bi-envelope",
        },
        {
            "name": "Portfolio",
            "url": "https://adhil-portfolio.onrender.com/",
            "icon": "bi-globe",
        },
    ]
    return render(request, "contact.html", {"social_accounts": social_accounts})
