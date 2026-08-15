from django.contrib import admin
from .models import HistoricalEvent


@admin.register(HistoricalEvent)
class HistoricalEventAdmin(admin.ModelAdmin):

    list_display = (
        "year",
        "title",
        "location",
    )

    list_filter = (
        "year",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )

    ordering = (
        "year",
    )