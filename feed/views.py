from django.shortcuts import render
from rest_framework import generics
from django.conf import settings

from posts.serializers import PostListSerializer
from posts.models import Post


class FeedAPIView(generics.ListAPIView):
    """ Users feed """

    serializer_class = PostListSerializer
    # user = self.request.user

    def get_queryset(self):
        return Post.objects.filter(user__owner__subscriber=self.request.user).order_by('-created') \
             .select_related('user').prefetch_related('comments')
