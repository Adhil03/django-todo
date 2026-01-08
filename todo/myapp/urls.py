from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("toggle_todo/<int:todo_id>/", views.toggle_todo, name="toggle_todo"),
    path("delete_todo/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("edit_todo/<int:todo_id>/", views.edit_todo, name="edit_todo"),
]
