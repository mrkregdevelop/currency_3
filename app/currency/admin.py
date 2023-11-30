from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder

from currency.models import Rate


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'source',
        'currency_type',
        'created'
    )
    list_filter = (
        'currency_type',
        ('created', DateRangeFilterBuilder())
    )
    search_fields = (
        'buy',
        'sell',
        'source',
    )
    readonly_fields = (
        'buy',
        'sell'
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request):
    #     return True
    #
    # def has_change_permission(self, request, obj=None):
    #     return False
