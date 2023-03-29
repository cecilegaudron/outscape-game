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
from django.contrib.messages.views import SuccessMessageMixin
# Import for send mail with contact form
from django.core.mail import send_mail


def index(request):
    """
    Basic view for Home Page
    """
    return render(request, 'index.html', {})


def game(request):
    """
    Basic view for Game Page
    """
    return render(request, 'game.html', {})


def contact(request):
    """
    Basic view for Contact Page
    """
    if request.method == "POST":
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_message = request.POST['contact-message']

        # Function sending the email
        send_mail(
            'Customer message from' + contact_name,  # subject
            contact_message,  # message
            contact_email,  # from email
            ['karaokeprototype153@simplelogin.com'],  # to email
            fail_silently=False,
            # Success message displays when the form is valid
            success_message="Your message has been sent successfully!"
        )
        return render(request, 'contact.html', {'contact_name': contact_name})
    else:
        return render(request, 'contact.html', {})


class AddBookingView(SuccessMessageMixin, CreateView):
    """
    This is the view for the booking form
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking.html'
    # Success message displays when the form is valid
    success_message = "Your booking is submitted. Your request pending. \
        The organizers must accept your booking."

    def form_invalid(self, form):
        """
        If the form is invalid a message is displaying for the user
        """
        messages.warning(self.request,
                         'There was a problem processing your booking.\
             Please double check below your information.')
        return super().form_invalid(form)


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
    queryset = Booking.objects.filter(
        status=1,
        bookdate__gte=now().date()
        ).order_by('bookdate')


class BookingDetailView(DetailView):
    """
    ClassBased View displaying the booking to the user
    """
    model = Booking
    template_name = 'booking_detail.html'


class UpdateBookingView(SuccessMessageMixin, UpdateView):
    """
    ClassBased View for the booking update
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking_update.html'
    success_message = "Your booking has been successfully updated!"

    def form_invalid(self, form):
        """
        If the form is invalid a message is displaying for the user
        """
        messages.warning(self.request,
                         'There was a problem processing your booking.\
             Please double check below your information.')
        return super().form_invalid(form)


class DeleteBookingView(SuccessMessageMixin, DeleteView):
    """
    ClassBased View for the booking remove
    """
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking-list')
    success_message = "Your booking has been successfully cancelled."
