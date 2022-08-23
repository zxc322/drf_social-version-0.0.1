from django.shortcuts import render
from rest_framework import generics, viewsets, status, permissions
from rest_framework.response import Response
from custom import classes, my_permissions

from .serializers import PostListSerializer, PostSerializer
from .models import Post


class PostListAPIView(generics.ListAPIView):
    """ Users (pk) posts """

    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk'))  # .select_related('user').prefetch_related('comments')


class PostView(classes.CreateRetrieveUpdateDestroy):
    """ Post CRUD"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [my_permissions.IsAuthor],
                                    'destroy': [my_permissions.IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

