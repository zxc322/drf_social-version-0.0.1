from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from .models import ExtendedUser, InterestsTags, OwnInterests


# class ChoseTagSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = InterestsTags
#         fields = ['name']

class UserListSerializer(serializers.ModelSerializer):
    """ Public info about  users"""

    avatar = serializers.ImageField(read_only=True)
    # interests_tags = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    # own_interests = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = ExtendedUser
        fields = [
            'id',
            'avatar',
            'username',
            'first_name',
            'last_name',
            'about_me',
            'birthday',
            'gender',
            'interests_tags',
            'own_interests',
            'is_active',
            'last_login',
            'date_joined'
        ]

        depth = 1


class UserCreateSerializer(serializers.ModelSerializer):
    """ Create or update users profile"""

    interests_tags = serializers.PrimaryKeyRelatedField(many=True, queryset=InterestsTags.objects.all())
    own_interests = serializers.PrimaryKeyRelatedField(many=True, queryset=OwnInterests.objects.all())

    class Meta:
        model = ExtendedUser
        fields = [
            'avatar',
            'username',
            'password',
            'email',
            'phone',
            'first_name',
            'last_name',
            'about_me',
            'birthday',
            'gender',
            'interests_tags',
            'own_interests'
        ]
        depth = 2

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                if attr == 'password':
                    password = validated_data['password']
                    instance.set_password(password)
                    continue
                setattr(instance, attr, value)

        instance.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance


class CreateOwnInterest(serializers.ModelSerializer):
    class Meta:
        model = OwnInterests
        fields = '__all__'



