from django.contrib import admin

from .models import IPO, IPOApplication


@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = (
        'issue_name',
        'security',
        'issue_price',
        'total_units',
        'minimum_units',
        'maximum_units',
        'opening_date',
        'closing_date',
        'status',
    )
    list_filter = (
        'status',
        'opening_date',
        'closing_date',
    )
    search_fields = (
        'issue_name',
        'security__symbol',
    )


@admin.register(IPOApplication)
class IPOApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'investor',
        'ipo',
        'requested_units',
        'allotted_units',
        'status',
        'applied_at',
        'processed_at',
    )
    list_filter = (
        'status',
        'applied_at',
    )
    search_fields = (
        'investor__client_id',
        'ipo__issue_name',
    )