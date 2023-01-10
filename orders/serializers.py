from rest_framework import serializers

from .models import Order
from menu.models import Menu
from menu.serializers import MenuSerializer


class OrderListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        items = [Order(**item) for item in validated_data]
        return Order.objects.bulk_create(items)


class OrderSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        source="item",
        write_only=True,
    )
    total_item_price = serializers.SerializerMethodField()

    def get_total_item_price(self, obj: Order) -> float:
        return obj.item.price * obj.quantity

    class Meta:
        model = Order
        fields = [
            "id",
            "quantity",
            "total_item_price",
            "payment",
            "item",
            "item_id",
        ]
        read_only_fields = ["item"]
        extra_kwargs = {
            "payment": {"required": False},
        }

        depth = 1
        list_serializer_class = OrderListSerializer
