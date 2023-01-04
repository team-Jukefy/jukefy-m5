from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class PaymentStatus(models.TextChoices):
    pending = "pending"
    paid = "paid"


class Order(models.Model):
    class Meta:
        ordering = ["id"]

    quantity = models.IntegerField(validators=[
            MaxValueValidator(99),
            MinValueValidator(1)
        ])
    payment = models.CharField(
        max_length=7,
        choices=PaymentStatus.choices,
    )

    item = models.ForeignKey(
        "menu.Menu",
        on_delete=models.CASCADE,
        related_name="item_orders"
    )

    table = models.ForeignKey(
        "tables.Table",
        on_delete=models.CASCADE,
        related_name="table_orders"
    )

    def __repr__(self) -> str:
        return f"<Order [{self.id}] - {self.table.table_name}>"
