from django.contrib import admin

from .models import FreedomFighter


@admin.register(FreedomFighter)
class FreedomFighterAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "birth_year",
        "death_year",
    )

    search_fields = (
        "name",
        "short_description",
        "biography",
    )

    list_filter = (
        "birth_year",
    )

    ordering = (
        "name",
    )