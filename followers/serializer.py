from rest_framework import serializers

from user.models import ExtendedUser
from .models import Follower


class FollowerListSerializer(serializers.ModelSerializer):
    subscriber_username = serializers.CharField(source='subscriber.username')
    subscriber_avatar = serializers.CharField(source='subscriber.avatar')

    class Meta:
        model = Follower
        fields = ['subscriber_id', 'subscriber_username', 'subscriber_avatar']


class IFollowSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username')
    user_avatar = serializers.CharField(source='user.avatar')

    class Meta:
        model = Follower
        fields = ['user_id', 'user_username', 'user_avatar']
