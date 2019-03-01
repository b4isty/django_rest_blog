from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import BlogSerializers
from .models import Blog
from rest_framework.generics import ListCreateAPIView


# class BlogView(ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers
#     permission_classes = [IsAuthenticatedOrReadOnly]


class BlogListView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


