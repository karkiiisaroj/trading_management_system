from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='investor'
    )
    client_id = models.CharField(
        max_length=20,
        unique=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.client_id} - {self.user.username}"


class Broker(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='broker'
    )
    broker_code = models.CharField(
        max_length=20,
        unique=True
    )
    name = models.CharField(
        max_length=100
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    email = models.EmailField(
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.broker_code} - {self.name}"