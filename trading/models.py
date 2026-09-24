from django.db import models

from accounts.models import Investor, Broker
from market.models import Security


class TradingAccount(models.Model):
    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        related_name='trading_accounts'
    )
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE,
        related_name='trading_accounts'
    )
    account_number = models.CharField(
        max_length=30,
        unique=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.account_number


class Order(models.Model):
    ORDER_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUBMITTED', 'Submitted'),
        ('EXECUTED', 'Executed'),
        ('PARTIALLY_EXECUTED', 'Partially Executed'),
        ('REJECTED', 'Rejected'),
        ('CANCELLED', 'Cancelled'),
    ]

    trading_account = models.ForeignKey(
        TradingAccount,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    security = models.ForeignKey(
        Security,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    order_type = models.CharField(
        max_length=10,
        choices=ORDER_TYPES
    )
    quantity = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"{self.trading_account.account_number} - "
            f"{self.order_type} - "
            f"{self.security.symbol}"
        )


class Trade(models.Model):
    STATUS_CHOICES = [
        ('EXECUTED', 'Executed'),
        ('SETTLED', 'Settled'),
    ]

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='trades'
    )
    quantity = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    execution_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    executed_at = models.DateTimeField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='EXECUTED'
    )

    def __str__(self):
        return f"Trade #{self.id} - {self.order.security.symbol}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    trade = models.OneToOneField(
        Trade,
        on_delete=models.CASCADE,
        related_name='transaction'
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )
    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Transaction #{self.id} - {self.transaction_type}"


class Holding(models.Model):
    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        related_name='holdings'
    )
    security = models.ForeignKey(
        Security,
        on_delete=models.CASCADE,
        related_name='holdings'
    )
    quantity = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    average_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['investor', 'security'],
                name='unique_investor_security_holding'
            )
        ]

    def __str__(self):
        return f"{self.investor.client_id} - {self.security.symbol}"


class BrokerInvestorAssignment(models.Model):
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE,
        related_name='investor_assignments'
    )
    investor = models.ForeignKey(
        Investor,
        on_delete=models.CASCADE,
        related_name='broker_assignments'
    )
    assigned_at = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['broker', 'investor'],
                name='unique_broker_investor_assignment'
            )
        ]

    def __str__(self):
        return f"{self.broker.broker_code} - {self.investor.client_id}"


class BrokerSecurityAssignment(models.Model):
    broker = models.ForeignKey(
        Broker,
        on_delete=models.CASCADE,
        related_name='security_assignments'
    )
    security = models.ForeignKey(
        Security,
        on_delete=models.CASCADE,
        related_name='broker_assignments'
    )
    assigned_at = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['broker', 'security'],
                name='unique_broker_security_assignment'
            )
        ]

    def __str__(self):
        return f"{self.broker.broker_code} - {self.security.symbol}"