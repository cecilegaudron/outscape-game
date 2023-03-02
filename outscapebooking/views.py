from django.shortcuts import render
from django.views import generic
from .models import Booking


# Bookings list 
class BookingList(generic.ListView):
    model = Booking
    # filter the bookings with confirmed status and order by date
    queryset = Boooking.objects.filter(status=1).order_by('-date')
    # the list view is display on the index page
    template_name = 'index.html'
    # If more of 6 bookings a new page is created
    paginate_by = 6
