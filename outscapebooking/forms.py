from django import forms
from django.forms import ModelForm
from .models import Booking
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

'''
https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
'''

TIMESLOT_LIST = (
    ("10:00-13:00", "10:00-13:00"),
    ("11:00-14:00", "11:00-14:00"),
    ("12:00-15:00", "12:00-15:00"),
    ("13:00-16:00", "13:00-16:00"),
    ("14:00-17:00", "14:00-17:00"),
    ("15:00-18:00", "15:00-18:00"),
    ("16:00-19:00", "16:00-19:00"),
    )


class BookingForm(ModelForm):

    class Meta:

        model = Booking

        # Fields required
        fields = ('first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment')