from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(blank=True, default=None, null=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=True)
