from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "contact",
            "username",
            "name",
            "is_staff",
            "is_superuser",
        ]
        read_only_fields = [
            "id",
            "is_superuser",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": False},
            "is_staff": {"required": False, "default": True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
