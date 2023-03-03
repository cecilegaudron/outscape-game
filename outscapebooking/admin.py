from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('date', 'timeslot', 'players', 'tickets', 'status', 'comment')
    list_filter = ('status', 'date')
