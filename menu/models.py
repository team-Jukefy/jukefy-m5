from django.db import models


class Categories(models.TextChoices):
    drinks = "drinks"
    foods = "foods"
    disserts = "disserts"


class Menu(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=8,
        choices=Categories.choices,
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=250)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="items"
    )

    def __repr__(self) -> str:
        return f"<Menu item [{self.id}] - {self.name}>"
