from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('date', 'hour', 'players', 'tickets', 'status', 'comment')
    search_fields = ['status', 'date']
    list_filter = ('status', 'date')
