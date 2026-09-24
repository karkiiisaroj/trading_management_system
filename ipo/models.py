from django.db import models

from accounts.models import Investor
from market.models import Security


class IPO(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    security = models.ForeignKey(
        Security,
        on_delete=models.CASCADE,
        related_name='ipos'
    )
    issue_name = models.CharField(
        max_length=150
    )
    issue_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    total_units = models.PositiveBigIntegerField()
    minimum_units = models.PositiveBigIntegerField()
    maximum_units = models.PositiveBigIntegerField()
    opening_date = models.DateField()
    closing_date = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='UPCOMING'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.issue_name


class IPOApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('ALLOTTED', 'Allotted'),
        ('PARTIALLY_ALLOTTED', 'Partially Allotted'),
        ('NOT_ALLOTTED', 'Not Allotted'),
    ]

    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        related_name='ipo_applications'
    )
    ipo = models.ForeignKey(
        IPO,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    requested_units = models.PositiveBigIntegerField()
    allotted_units = models.PositiveBigIntegerField(
        default=0
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    applied_at = models.DateTimeField(
        auto_now_add=True
    )
    processed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['investor', 'ipo'],
                name='unique_investor_ipo_application'
            )
        ]

    def __str__(self):
        return f"{self.investor.client_id} - {self.ipo.issue_name}"