from django.db import models

from accounts.models import Investor


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('ORDER', 'Order'),
        ('TRADE', 'Trade'),
        ('IPO', 'IPO'),
        ('TRANSACTION', 'Transaction'),
        ('SYSTEM', 'System'),
    ]

    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    title = models.CharField(
        max_length=150
    )
    message = models.TextField()
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    is_read = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.investor.client_id} - {self.title}"