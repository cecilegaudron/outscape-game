from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Booking
from django.utils.timezone import now
from datetime import date


# Bookings list 
class BookingList(generic.ListView):
    model = Booking
    '''
    Filter the bookings with confirmed status
    Display only futur bookings
    https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django/4668703#4668703
    Order by date
    '''
    queryset = Booking.objects.filter(status=1, bookdate__gte=now().date()).order_by('bookdate')
    # the list view is display on the index page
    template_name = 'index.html'
    # If more of 6 bookings a new page is created
    paginate_by = 10