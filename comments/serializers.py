from rest_framework import serializers

from .models import Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    """ Comments filter (parents only) """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


# class RecursiveSerializer(serializers.Serializer):
#     """ All comments recursively"""
#
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer.data


class CreateCommentSerializer(serializers.ModelSerializer):
    """ Create comment """

    class Meta:
        model = Comment
        fields = ("post", "text", "parent")


class ListCommentSerializer(serializers.ModelSerializer):
    """ Posts comments """
    text = serializers.SerializerMethodField()
    # children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created", "updated", "deleted", "comments_count", "likes_count")  # , "children")


class Comment2CommentSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()
    # children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        model = Comment
        fields = ("id", "user", "text", "created", "updated", "deleted", "comments_count")
