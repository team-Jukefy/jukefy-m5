from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from menu.models import Menu
from tables.models import Table


class PaymentStatus(models.TextChoices):
    pending = "pending"
    paid = "paid"


class Order(models.Model):
    class Meta:
        ordering = ["id"]

    quantity = models.IntegerField(
        validators=[MaxValueValidator(99), MinValueValidator(1)]
    )
    payment = models.CharField(
        max_length=7,
        choices=PaymentStatus.choices,
        default=PaymentStatus.pending,
    )

    item = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="item_orders"
    )

    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="table_orders"
    )

    def __repr__(self) -> str:
        return f"<Order [{self.id}] - {self.table.table_number}>"
