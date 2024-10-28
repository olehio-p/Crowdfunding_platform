from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils import timezone
from Crowdfunding_platform.models.user_models.CustomUser import CustomUser
from Crowdfunding_platform.serializers.user_serializers.language_serializer import LanguageSerializer
from Crowdfunding_platform.serializers.user_serializers.location_serializer import LocationSerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class CustomUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    language = LanguageSerializer(required=False, allow_null=True)
    location = LocationSerializer(required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'user', 'profile_picture', 'bio', 'user_type',
            'join_date', 'phone_number', 'language', 'location'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            username=user_serializer.validated_data['username'],
            password=user_serializer.validated_data['password'],
            email=user_serializer.validated_data['email'],
            first_name=user_serializer.validated_data.get('first_name', ''),
            last_name=user_serializer.validated_data.get('last_name', '')
        )

        custom_user = CustomUser.objects.create(user=user, **validated_data)
        return custom_user