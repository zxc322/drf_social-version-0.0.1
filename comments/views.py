from django.shortcuts import render
from rest_framework import permissions, generics

from custom.classes import CreateUpdateDestroy
from custom.my_permissions import IsAuthor
from .models import Comment
from .serializers import CreateCommentSerializer, ListCommentSerializer, Comment2CommentSerializer


class CommentsView(CreateUpdateDestroy):
    """ CRUD комментариев к запси
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().select_related('children')
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def perform_destroy(self, instance):
    #     instance.deleted = True
    #     instance.save()


class Comment2Comment(generics.ListAPIView):

    serializer_class = Comment2CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(
            parent=self.kwargs.get('pk'))
