from django.db import models


class Company(models.Model):
    name = models.CharField(
        max_length=150
    )
    registration_number = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField(
        blank=True
    )
    sector = models.CharField(
        max_length=100,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Security(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='securities'
    )
    symbol = models.CharField(
        max_length=20,
        unique=True
    )
    name = models.CharField(
        max_length=150
    )
    security_type = models.CharField(
        max_length=50
    )
    isin = models.CharField(
        max_length=50,
        unique=True
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.symbol} - {self.name}"


class MarketData(models.Model):
    security = models.ForeignKey(
        Security,
        on_delete=models.CASCADE,
        related_name='market_data'
    )
    trading_date = models.DateField()

    open_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    high_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    low_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    close_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    volume = models.BigIntegerField()

    turnover = models.DecimalField(
        max_digits=18,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['security', 'trading_date'],
                name='unique_security_trading_date'
            )
        ]

    def __str__(self):
        return f"{self.security.symbol} - {self.trading_date}"