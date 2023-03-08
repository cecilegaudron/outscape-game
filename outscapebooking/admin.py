from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('bookdate', 'timeslot', 'players', 'tickets', 'status', 'comment')
    list_filter = ('status', 'bookdate')

# Remove the default groups
# https://www.section.io/engineering-education/customizing-django-admin/
admin.site.unregister(Group)