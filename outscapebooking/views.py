from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Booking


# Bookings list 
class BookingList(generic.ListView):
    model = Booking
    # filter the bookings with confirmed status and order by date
    queryset = Booking.objects.filter(status=1).order_by('bookdate')
    # the list view is display on the index page
    template_name = 'index.html'
    # If more of 6 bookings a new page is created
    paginate_by = 6


# New Try for Views
class BookingView(TemplateView):
    template_name = 'index.html'