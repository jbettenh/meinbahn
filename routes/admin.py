from django.contrib import admin
from .models import Route


class RoutesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Stop ID',                      {'fields': ['stop_id']}),
        ('Direction',               {'fields': ['direction']})
    ]
    list_display = ('stop_id','direction')

admin.site.register(Route, RoutesAdmin)