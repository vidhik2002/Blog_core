from django.shortcuts import render
from rest_framework import generics
from blog.models import *
from .serializers import PostSerializer

# Create your views here.


class PostList(generics.ListCreateAPIView):
    query_set = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveDestroyAPIView):
    pass

