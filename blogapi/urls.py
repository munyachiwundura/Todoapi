from django.urls import path
from blogapi import views

urlpatterns = [
    path("", views.apiOverview, name="overview"),
    path("blogs", views.blogposts, name="All posts"),
    path("featured_blogs/<str:pk>/", views.featuredblogposts, name="Featured posts"),
    path("blogposts/<str:pk>/", views.blogpost, name="Blog Post"),
]
