from rest_framework import serializers

from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

    class Meta:
        model = Menu
        fields = [
            "id",
            "name",
            "category",
            "price",
            "description",
            "user_id",
        ]
