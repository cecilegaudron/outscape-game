# Import to deploy view
from django.shortcuts import render
# Import differents views
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# Import for date on booking form
from django.utils.timezone import now
from datetime import date
# Import reverse URL resolver apply only if the value is needed
from django.urls import reverse_lazy
# Import form and model
from .forms import BookingForm
from .models import Booking
# Import store function for future reference
from django.utils.functional import cached_property
# Import for messaging system
from django.contrib import messages
# Import for send mail with contact form
from django.core.mail import send_mail


# Basic view for Home Page
def index(request):
    return render(request, 'index.html', {})


# Basic view for Game Page
def game(request):
    return render(request, 'game.html', {})


# Basic view for Contact Page
def contact(request):
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_message = request.POST['contact-message']

        # Function sending the email
        send_mail(
            'Customer message from' + contact_name, # subject
            contact_message, # message
            contact_email, # from email
            ['karaokeprototype153@simplelogin.com'], # to email
            fail_silently=False,
        )
        return render(request, 'contact.html', {'contact_name': contact_name})
    else:
        return render(request, 'contact.html', {})


"""
This is the view for the booking form 
"""
class AddBookingView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'

"""
    # This is the view for the Booking form
    def make_booking(request):
        if request.method == "POST":
            form = BookingForm(request.POST)
            # If else loop with valid condition for saving data
            if form.is_valid():
                form.save()
            else:
                messages.error(request, ('There is an error on your form, please try again'))
                return render(request, 'booking.html', {})

            messages.success(request, ('Your booking has been submitted successfully'))
            return render(request, 'booking_list.html', {})
        else:
            return render(request, 'booking.html', {})
"""


"""
ClassBased View for the booking list
Filter the bookings with confirmed status
Display only futur bookings
https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django/4668703#4668703
Order by date
"""
class BookingList(ListView):
    model = Booking
    template_name = 'booking_list.html'
    queryset = Booking.objects.filter(status=1, bookdate__gte=now().date()).order_by('bookdate')


"""
ClassBased View displaying the booking to the user
"""
class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'


"""
ClassBased View for the booking update
IF NEEDED OTHERS FIELDS THAN BOOKING, JUST CREATE A NEW FORM JUST FOR THE UPDATE
"""
class UpdateBookingView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_update.html'


"""
ClassBased View for the booking remove
"""
class DeleteBookingView(DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking-list')