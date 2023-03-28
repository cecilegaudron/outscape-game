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
    #booking = Booking.booking_id
    #queryset = Booking.objects.filter(status=1)
    template_name = 'booking_detail.html'
    #fields = ['first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment']


"""
ClassBased View for the booking update
IF NEEDED OTHERS FIELDS THAN BOOKING, JUST CREATE A NEW FORM JUST FOR THE UPDATE
"""
class UpdateBookingView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_update.html'
    #fields = ['first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment']


"""
ClassBased View for the booking remove
"""
class DeleteBookingView(DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking-list')


"""
Define functions for error pages
https://blog.juanwolf.fr/fr/posts/programming/comment-creer-une-page-404-django/

def page_not_found_view(request):
     return render(request,'404.html')
"""

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