from django.contrib import admin

from .models import (
    TradingAccount,
    Order,
    Trade,
    Transaction,
    Holding,
    BrokerInvestorAssignment,
    BrokerSecurityAssignment,
)


@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):
    list_display = (
        'account_number',
        'investor',
        'broker',
        'is_active',
        'created_at',
    )
    list_filter = (
        'is_active',
        'broker',
    )
    search_fields = (
        'account_number',
        'investor__client_id',
        'broker__broker_code',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'trading_account',
        'security',
        'order_type',
        'quantity',
        'price',
        'status',
        'created_at',
    )
    list_filter = (
        'order_type',
        'status',
        'security',
    )
    search_fields = (
        'trading_account__account_number',
        'security__symbol',
    )


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'quantity',
        'execution_price',
        'executed_at',
        'status',
    )
    list_filter = (
        'status',
        'executed_at',
    )
    search_fields = (
        'order__security__symbol',
        'order__trading_account__account_number',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'trade',
        'transaction_type',
        'amount',
        'status',
        'created_at',
    )
    list_filter = (
        'transaction_type',
        'status',
    )
    search_fields = (
        'trade__order__security__symbol',
    )


@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = (
        'investor',
        'security',
        'quantity',
        'average_cost',
        'updated_at',
    )
    search_fields = (
        'investor__client_id',
        'security__symbol',
    )


@admin.register(BrokerInvestorAssignment)
class BrokerInvestorAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'broker',
        'investor',
        'assigned_at',
        'is_active',
    )
    list_filter = (
        'is_active',
        'broker',
    )
    search_fields = (
        'broker__broker_code',
        'investor__client_id',
    )


@admin.register(BrokerSecurityAssignment)
class BrokerSecurityAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'broker',
        'security',
        'assigned_at',
        'is_active',
    )
    list_filter = (
        'is_active',
        'broker',
    )
    search_fields = (
        'broker__broker_code',
        'security__symbol',
    )