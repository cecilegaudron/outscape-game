from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Booking

""" 
The Blog entry is accessible from the Admin panel
Possible to choose which fields are display
Possible to choose which fields can be filter
"""
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('bookdate', 'timeslot', 'players', 'tickets', 'status', 'comment', 'player_name', 'booking_id', 'created_on')
    list_filter = ('status', 'bookdate')

""" 
Remove the default groups
https://www.section.io/engineering-education/customizing-django-admin/
 """
admin.site.unregister(Group)