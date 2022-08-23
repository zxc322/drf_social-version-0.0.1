from rest_framework import serializers

from .models import PostLike, CommentLike
from user.serializers import UserListSerializer


class UsersLikedPostSerializer(serializers.ModelSerializer):
    """ User who has liked Post serializer """

    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    user_avatar = serializers.ImageField(source='user.avatar')

    class Meta:
        model = PostLike

        fields = ['user', 'user_id', 'user_avatar']


class UsersLikedCommentSerializer(serializers.ModelSerializer):
    """ User who has liked Comment serializer """

    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    user_avatar = serializers.ImageField(source='user.avatar')

    class Meta:
        model = CommentLike

        fields = ['user', 'user_id', 'user_avatar']