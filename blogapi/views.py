from django.shortcuts import render
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapi.models import BlogPost
from blogapi.serializers import BlogPostSerializer

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "All blog Posts": reverse(blogposts, request=request),
        "Single Blog Post": reverse(blogpost, args=[1], request=request),
    }
    return Response(api_urls)


@api_view(["GET"])
def blogposts(request):
    todo_items = BlogPost.objects.all()
    serializer = BlogPostSerializer(todo_items, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def featuredblogposts(request):
    todo_items = BlogPost.objects.filter(featured=True)
    serializer = BlogPostSerializer(todo_items, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def blogpost(request, pk):
    todo_items = BlogPost.objects.get(id=pk)
    serializer = BlogPostSerializer(todo_items, many=False)
    return Response(serializer.data)
