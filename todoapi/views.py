from django.shortcuts import render
from rest_framework import serializers
from django.urls import path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from todoapi.models import TodoItem
from todoapi.serializers import TodoItemSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.models import Token


# Create your views here.

@permission_classes([IsAuthenticated])
@api_view(["GET"])
def apiOverview(request):
    api_urls = {"Posts": "/Posts/"}
    return Response(api_urls)


@permission_classes([IsAuthenticated])
@api_view(["GET"])
def todos(request):
    user = request.user
    todo_items = TodoItem.objects.filter(user=user)
    serializer = TodoItemSerializer(todo_items, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def addtodo(request):
    serializer = TodoItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(["POST"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def updatetodo(request, pk):
    task = TodoItem.objects.get(id=pk)
    serializer = TodoItemSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(["DELETE"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def deletetodo(request, pk):
    task = TodoItem.objects.get(id=pk)
    task.delete()

    return Response(f"item {pk} was deleted")
