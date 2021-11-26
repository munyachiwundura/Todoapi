from django.urls import path
from todoapi import views


urlpatterns = [
    path("", views.apiOverview, name="overview"),
    path("todoitems", views.todos, name="View all todos"),
    path("addtodo", views.addtodo, name="Add an item"),
    path("updatetodo/<str:pk>/", views.updatetodo, name="Update and item"),
    path("deletetodo/<str:pk>/", views.deletetodo, name="Delete an Item"),
]
