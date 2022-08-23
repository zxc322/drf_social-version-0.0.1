from django.shortcuts import render
from rest_framework import generics, permissions, views, response

from .serializer import FollowerListSerializer, IFollowSerializer
from .models import Follower
from user.models import ExtendedUser


class MyFollowersView(generics.ListAPIView):
    """ List of my subscribers """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user).select_related('subscriber')


class UsersIFollowView(generics.ListAPIView):
    """ List of users that I'm following """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = IFollowSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscriber=self.request.user).select_related('user')


class UsersFollowersView(generics.ListAPIView):
    """ List of users (pk) subscribers """

    serializer_class = FollowerListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.kwargs.get('pk')).select_related('subscriber')


class UserFollowsView(generics.ListAPIView):
    """ List of users that user (pk) follows """

    serializer_class = IFollowSerializer

    def get_queryset(self):
        return Follower.objects.filter(subscriber=self.kwargs.get('pk')).select_related('user')


class AddRemoveFollowerView(views.APIView):
    """ Add/remove follower status """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            user = ExtendedUser.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.get_or_create(subscriber=request.user, user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)
