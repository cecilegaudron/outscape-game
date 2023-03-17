from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.views.generic import TemplateView
from django.utils.timezone import now
from datetime import date
from .forms import BookingForm
from .models import Booking

"""
This is the view for the Booking form
# https://www.youtube.com/watch?v=CVEKe39VFu8
"""
def make_booking(request):
    # Not load again the form if the user already submitted it
    submitted = False
    if request.method == "POST":
        form = BookingForm(request.POST)
        
        # If else loop with valid condition for saving data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('booking.html?submitted=True')
    else:
        form = BookingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, "booking.html", {'form': form, 'submitted': submitted})

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
    # The list view is display on the index page
    template_name = 'index.html'
    # If more of 6 bookings a new page is created
    paginate_by = 10