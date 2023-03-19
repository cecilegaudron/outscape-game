from django.shortcuts import render, get_object_or_404
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

"""
# Display the booking to the user
class MyBooking(View):

    def get(self, request):
        query set

        if request.user.is_authenticated:
            reservation = get_object_or_404(Booking, id=reservation_id)
            current_user = request.user

            if current_user == reservation.user:
                context = {
                    "Your booking is the:": reservation.bookdate,
                    "At:": reservation.timeslot
                }
            else:
                return redirect(reverse("booking"))
        else:
            return redirect(reverse("account_login"))
"""

class MyBooking(View):

    def get(self, request, *args, **kwargs):
        """
        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(queryset)

        return render(
            request,
            "booking_detail.html",
            {
                "Your booking": booking,
                "submitted": False,
            },
        )
        """
        if request.user.is_authenticated:
            booking = Booking.objects.filter(user=request.user)

            return render(
                request, 'booking.html',
                {
                    'bookings': bookings,
                },
            )

        else:
            return redirect(reverse("account_login"))
    
    def post(self, request, *args, **kwargs):

        queryset = Booking.objects.filter(status=1)
        booking = get_object_or_404(queryset)

        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking = booking_form.save(commit=False)
            booking.save()
        else:
            booking_form = BookingForm()

        return render(
            request,
            "booking_detail.html",
            {
                "Your booking": booking,
                "submitted": True,
            },
        )