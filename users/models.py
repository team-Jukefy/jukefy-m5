from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    username = models.CharField(
        null=True,
        max_length=150,
        unique=True,
    )
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    is_staff = models.BooleanField(default=True)
    contact = models.CharField(
        max_length=150,
        null=True,
    )
