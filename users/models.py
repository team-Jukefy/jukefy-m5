from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=127,
        unique=True,
        error_messages={
            "unique": "This field must be unique.",
        },
    )
