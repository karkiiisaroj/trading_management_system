from django.contrib import admin
from .models import Company, Security, MarketData


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'registration_number',
        'sector',
        'is_active',
        'created_at',
    )
    list_filter = (
        'is_active',
        'sector',
    )
    search_fields = (
        'name',
        'registration_number',
    )


@admin.register(Security)
class SecurityAdmin(admin.ModelAdmin):
    list_display = (
        'symbol',
        'name',
        'company',
        'security_type',
        'isin',
        'is_active',
        'created_at',
    )
    list_filter = (
        'is_active',
        'security_type',
    )
    search_fields = (
        'symbol',
        'name',
        'isin',
        'company__name',
    )


@admin.register(MarketData)
class MarketDataAdmin(admin.ModelAdmin):
    list_display = (
        'security',
        'trading_date',
        'open_price',
        'high_price',
        'low_price',
        'close_price',
        'volume',
        'turnover',
    )
    list_filter = (
        'trading_date',
        'security',
    )
    search_fields = (
        'security__symbol',
    )