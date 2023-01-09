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


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        extra_kwargs = {"music_name": {"write_only": True}}
        exclude = ["status"]
