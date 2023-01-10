from rest_framework import serializers

from .models import Order


class OrderListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        items = [Order(**item) for item in validated_data]
        return Order.objects.bulk_create(items)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "quantity", "payment", "item", "table"]
        extra_kwargs = {
            "payment": {"required": False},
            "table": {"required": False}
        }

        list_serializer_class = OrderListSerializer
