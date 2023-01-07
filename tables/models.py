from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TableStatus(models.TextChoices):
    available = "available"
    occupied = "occupied"


class Table(models.Model):
    class Meta:
        ordering = ["id"]

    table_number = models.IntegerField(
        unique=True, validators=[MaxValueValidator(99), MinValueValidator(1)]
    )
    status = models.CharField(
        max_length=9,
        choices=TableStatus.choices,
        default=TableStatus.available,
    )
    musics_count = models.IntegerField(
        validators=[
            MaxValueValidator(2),
            MinValueValidator(0),
        ],
        default=0,
    )
    user = models.OneToOneField(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="table",
        blank=True,
        null=True,
    )

    def __repr__(self) -> str:
        return f"<Table [{self.id}] - {self.table_number}>"
