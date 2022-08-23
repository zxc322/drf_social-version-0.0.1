from django.shortcuts import render
from rest_framework import views, permissions, response, generics

from .models import PostLike, CommentLike
from posts.models import Post
from comments.models import Comment
from .serializers import UsersLikedPostSerializer, UsersLikedCommentSerializer


class AddRemoveLikeView(views.APIView):
    """ Add/remove post/comment like """

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, slug, pk):
        if slug == 'post':
            try:
                post = Post.objects.get(id=pk)
            except Post.DoesNotExist:
                return response.Response(status=404)
            PostLike.objects.get_or_create(user=request.user, post=post)
            return response.Response(status=201)

        elif slug == 'comment':
            try:
                comment = Comment.objects.get(id=pk)
            except Comment.DoesNotExist:
                return response.Response(status=404)
            CommentLike.objects.get_or_create(user=request.user, comment=comment)
            return response.Response(status=201)

    def delete(self, request, slug, pk):
        if slug == 'post':
            try:
                like = PostLike.objects.get(user=request.user, post_id=pk)
            except PostLike.DoesNotExist:
                return response.Response(status=404)
            like.delete()
            return response.Response(status=204)

        elif slug == 'comment':
            try:
                like = CommentLike.objects.get(user=request.user, comment_id=pk)
            except CommentLike.DoesNotExist:
                return response.Response(status=404)
            like.delete()
            return response.Response(status=204)


class LikedPostUsersListAPIView(generics.ListAPIView):
    """ List of users who has liked post """

    serializer_class = UsersLikedPostSerializer

    def get_queryset(self):
        return PostLike.objects.filter(
            post_id=self.kwargs.get('pk'))


class LikedCommentUsersListAPIView(generics.ListAPIView):
    """ List of users who has liked comment """

    serializer_class = UsersLikedCommentSerializer

    def get_queryset(self):
        return CommentLike.objects.filter(
            comment_id=self.kwargs.get('pk'))
