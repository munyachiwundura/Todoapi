from django.urls import path
from projects_api import views

urlpatterns = [
    path("", views.apiOverview, name="overview"),
    path("projects", views.projects, name="All Projects"),
    path("projects/<str:pk>/", views.project, name="Project"),
    path("projects/<str:pk>/images/", views.projectImages, name="Project"),
]
