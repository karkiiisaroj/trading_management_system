from django.contrib import admin
from .models import Investor, Broker


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = (
        'client_id',
        'user',
        'phone',
        'is_active',
        'created_at',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'client_id',
        'user__username',
        'user__email',
    )


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = (
        'broker_code',
        'name',
        'user',
        'phone',
        'email',
        'is_active',
        'created_at',
    )
    list_filter = (
        'is_active',
    )
    search_fields = (
        'broker_code',
        'name',
        'user__username',
        'email',
    )