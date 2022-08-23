from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins, permissions, generics

from .serializers import *
from .models import *


class ListUsers(generics.ListAPIView):
    queryset = ExtendedUser.objects.all().prefetch_related('interests_tags', 'own_interests')
    # queryset = ExtendedUser.objects.all()
    serializer_class = UserListSerializer


class CreateUser(generics.CreateAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserCreateSerializer


class CreateOwnInterest(generics.CreateAPIView):
    queryset = OwnInterests.objects.all()
    serializer_class = CreateOwnInterest


class RetApiView(generics.RetrieveAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = UserListSerializer


class UpdDelApiView(generics.DestroyAPIView, generics.UpdateAPIView):
    # queryset = ExtendedUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        print('userID:', self.request.user.id)
        return ExtendedUser.objects.filter(id=self.request.user.id)
