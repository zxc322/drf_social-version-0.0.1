from rest_framework import serializers

from comments.serializers import ListCommentSerializer
from .models import Post
from comments.models import Comment


class PostListSerializer(serializers.ModelSerializer):
    """ Post serializer """

    image = serializers.ImageField(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    view_count = serializers.CharField(read_only=True)


    # comments = ListCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post

        fields = ['id', 'created', 'image', 'user', 'text', 'comments_count', 'likes_count', 'view_count']


class PostSerializer(serializers.ModelSerializer):
    """ Post serializer """

    image = serializers.ImageField(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    view_count = serializers.CharField(read_only=True)

    comments = ListCommentSerializer(many=True, read_only=True)
    # comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.filter(post_id=4))

    class Meta:
        model = Post

        fields = ['id', 'created', 'image', 'user', 'text', 'comments_count', 'likes_count', 'view_count', 'comments']


