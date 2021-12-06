from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework import serializers
from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from todoapi.models import TodoItem
from todoapi.serializers import TodoItemSerializer, RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.


# API Overview


@api_view(["GET"])
def apiOverview(request):
    base_url = reverse(apiOverview, request=request)
    api_urls = {
        "All Todos": reverse(todos, request=request),
        "All Analytics": reverse(allAnalytics, request=request),
        "Weekly Analytics": reverse(weeklyAnalytics, request=request),
        "Monthly Analytics": reverse(monthlyAnalytics, request=request),
        "Add an Item": reverse(addtodo, request=request),
        "Update and Item": reverse(updatetodo, args=[1], request=request),
        "Delete and Item": reverse(deletetodo, args=[1], request=request),
        "Register": reverse(register, request=request),
        "Access Token": f"{base_url}token/",
        "Refresh Token": f"{base_url}token/refresh/",
    }
    return Response(api_urls)


# Register User


@csrf_exempt
@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data["response"] = "new user sucessfully created"
        data["email"] = account.email
        data["username"] = account.username
    else:
        data = serializer.errors
    return Response(data)


# Get Todo Items


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def todos(request):
    user = request.user
    todo_items = TodoItem.objects.filter(user=user)
    serializer = TodoItemSerializer(todo_items, many=True)
    return Response(serializer.data)


# Add Todo Item


@permission_classes([IsAuthenticated])
@api_view(["POST"])
@csrf_exempt
def addtodo(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Update Todo Item


@permission_classes([IsAuthenticated])
@api_view(["POST"])
@csrf_exempt
def updatetodo(request, pk):
    task = TodoItem.objects.get(id=pk)
    serializer = TodoItemSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Delete Todo Item


@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
@csrf_exempt
def deletetodo(request, pk):
    task = TodoItem.objects.get(id=pk)
    task.delete()

    return Response(f"item {pk} was deleted")


##### todoItems analytics #####


# weekly analytics


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def weeklyAnalytics(request):

    user = request.user
    data = {}
    next_seven_days = []
    day_one = datetime.strptime(request.data["end_date"], "%Y-%m-%d")

    for n in range(1, 7):
        next_seven_days.append(str(day_one + timedelta(days=n))[0:10])

    for day in next_seven_days:
        data[day] = {
            "total": len(TodoItem.objects.filter(end_date=day, user=user)),
            "done": len(
                TodoItem.objects.filter(end_date=day).filter(status=True, user=user)
            ),
        }

    return Response(data)


# Monthy Analytics


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def monthlyAnalytics(request):

    user = request.user
    month = request.data["month"]
    data = {
        "month": datetime.date(1900, int(month), 1).strftime("%B"),
        "total": len(TodoItem.objects.filter(end_date__month=month, user=user)),
        "done": len(
            TodoItem.objects.filter(end_date__month=month).filter(
                status=True, user=user
            )
        ),
    }
    return Response(data)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def allAnalytics(request):

    user = request.user
    data = {
        "total": len(TodoItem.objects.filter(user=user)),
        "done": len(TodoItem.objects.filter(status=True, user=user)),
    }

    return Response(data)
