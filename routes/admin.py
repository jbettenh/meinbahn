from django.contrib import admin

from .models import Route


class RoutesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Route Name", {"fields": ["name"]}),
        ("Stop ID", {"fields": ["stop_id"]}),
        ("Direction", {"fields": ["direction"]}),
    ]
    list_display = ("name", "stop_id", "direction")


admin.site.register(Route, RoutesAdmin)
