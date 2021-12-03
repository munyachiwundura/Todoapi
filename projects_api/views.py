from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects_api.models import Project, Image
from projects_api.serializers import ProjectSerializer, ImageSerializer

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {"Posts": "/Posts/"}
    return Response(api_urls)


@api_view(["GET"])
def projects(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def featuredProjects(request):
    project = Project.objects.filter(featured=True)
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def project(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def projectImages(request, pk):
    project = Project.objects.get(id=pk)
    images = Image.objects.filter(project=project)
    images_serialized = ImageSerializer(images, many=True)
    return Response(images_serialized.data)
