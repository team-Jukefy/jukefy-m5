from rest_framework import serializers

from .models import Order
import ipdb

class OrderSerializer(serializers.ModelSerializer):



    def create(self, validated_data) -> Order:

        ipdb.set_trace()
        Order.objects.bulk_create(validated_data)
        return super().create(validated_data)
     
    class Meta:
        model = Order
        fields = [
            "id",
            "quantity",
            "payment",
            "item_id",
            "table_id",
        ]
        extra_kwargs = {"payment":{"required": False}}
        depth = 1
    
  
