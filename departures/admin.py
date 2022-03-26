from django.contrib import admin
from .models import Departure


class DepartureAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Line',                      {'fields': ['line']}),
        ('Destination',               {'fields': ['destination']}),
        ('Date information', {'fields': ['next_train_time'], 'classes': ['collapse']}),
    ]
    list_display = ('line','destination','next_train_time')


admin.site.register(Departure, DepartureAdmin)