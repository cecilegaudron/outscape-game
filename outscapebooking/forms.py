from django import forms
from django.forms import ModelForm
from .models import Booking
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.forms.fields import DateField

'''
https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
'''

# Creation of custom widget for a calendar
# https://stackoverflow.com/questions/42165163/how-do-i-use-a-datepicker-on-a-simple-django-form
class DateInput(forms.DateInput):
    input_type = 'date'

# Form class
class BookingForm(ModelForm):

    # Calendar call
    bookdate = forms.DateField(widget=DateInput)

    class Meta:

        model = Booking

        # Fields required
        fields = ('first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment')

