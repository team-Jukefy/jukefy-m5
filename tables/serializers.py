from rest_framework import serializers

from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = [
            "id",
            "table_number",
            "status",
            "musics_count",
        ]

    def create(self, validated_data):
        return Table.objects.create(**validated_data)
