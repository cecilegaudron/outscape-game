from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
#from django.views import generic, View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.timezone import now
from datetime import date
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking


# Basic view for Home Page
def index(request):
    return render(request, 'index.html', {})

"""
This is the view for the Booking form
THIS IS WORKING BUT THE ID IS NOT LINK WITH THE ID USER
# https://www.youtube.com/watch?v=CVEKe39VFu8

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
"""


class AddBookingView(CreateView):
    """
    This is the view for the booking form 
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    #fields = ('player_name', 'first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment')


class BookingList(ListView):
    """
    ClassBased View for the booking list
    Filter the bookings with confirmed status
    Display only futur bookings
    https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django/4668703#4668703
    Order by date
    """
    model = Booking
    template_name = 'booking_list.html'
    queryset = Booking.objects.filter(status=1, bookdate__gte=now().date()).order_by('bookdate')


class BookingDetailView(DetailView):
    """
    ClassBased View displaying the booking to the user
    """
    model = Booking
    #booking = Booking.booking_id
    #queryset = Booking.objects.filter(status=1)
    template_name = 'booking_detail.html'
    #fields = ['first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment']


class UpdateBookingView(UpdateView):
    """
    ClassBased View for the booking update
    IF NEEDED OTHERS FIELDS THAN BOOKING, JUST CREATE A NEW FORM JUST FOR THE UPDATE
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking_update.html'
    #fields = ['first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment']


class DeleteBookingView(DeleteView):
    """
    ClassBased View for the booking remove
    """
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking-list')


    """
    VOIR SI UTILE
    AUPARAVANT CETAIT DANS BOOKINGDETAILVIEW
    def detail_booking(request, booking_id):
    #def get(self, request, booking_id, *args, **kwargs):
        
        if request.user.is_authenticated:
            reservation = get_object_or_404(Booking, id=booking_id)
            #model = Booking
            current_user = request.user

            if current_user == reservation.user:
                context = {
                    "id": reservation.booking_id,
                    "date": reservation.bookdate,
                    "time": reservation.timeslot
                }
        else:
            return redirect(reverse("account_login"))

            #player_name = current_user
            #queryset = Booking.objects.filter(status=1, bookdate__gte=now().date())


            return render(
                request, 
                "booking_detail.html",
                {
                    "booking": Booking,
                    "user": Booking.player_name,
                    "id": Booking.booking_id
                },
            )
        else:
            return redirect(reverse("account_login"))

        if request.user.is_authenticated:
            model = Booking
            
            booking = get_object_or_404(Booking, booking_id=booking_id)
            current_user = request.user
            player_name = current_user
            #queryset = Booking.objects.filter(status=1, bookdate__gte=now().date())
        
        else:
            return redirect(reverse("account_login"))


class MyBooking(View):

    def get(self, request):

        if request.user.is_authenticated:
            model = Booking
            #reservation = get_object_or_404(Booking, id=booking_id)
            current_user = request.user
            player_name = current_user
            queryset = Booking.objects.filter(status=1, bookdate__gte=now().date())

            if current_user == player_name:
                #template_name = 'booking-detail'
                #return HttpResponseRedirect('booking_detail.html')
                booking = Booking.objects.filter(player_name)

                context = {
                    "Your booking is the:": bookdate,
                    "At:": timeslot,
                    "Info": comment
                }

            else:
                return redirect(reverse("booking"))
        else:
            return redirect(reverse("account_login"))


class MyBooking(View):

    def get(self, request, *args, **kwargs):
        model = Booking
        queryset = Booking.objects.filter(status=1, bookdate__gte=now().date())
        # The list view is display on the index page
        template_name = 'booking-detail'

class MyBooking(View):

    def get(self, request, *args, **kwargs):
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
        if request.user.is_authenticated:
            booking = Booking.objects.filter(user=request.user)

            return render(
                request, 'booking.html',
                {
                    'bookings': booking,
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
"""