from django.urls import path
from todoapi import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.apiOverview, name="overview"),
    path("todoitems", views.todos, name="View all todos"),
    path("addtodo", views.addtodo, name="Add an item"),
    path("analytics/", views.allAnalytics, name="All Analytics"),
    path("analytics/weekly", views.weeklyAnalytics, name="Weekly Analytics"),
    path("analytics/monthly", views.monthlyAnalytics, name="Monthly Analytics"),
    path("updatetodo/<str:pk>/", views.updatetodo, name="Update and item"),
    path("deletetodo/<str:pk>/", views.deletetodo, name="Delete an Item"),
    path("register", views.register, name="Add an item"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
