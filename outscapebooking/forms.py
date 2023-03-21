from django import forms
#from django.forms import ModelForm
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

""" 
Add styles to booking form
Choose which fields are display to the user
"""
class BookingForm(forms.ModelForm):

    bookdate = forms.DateField(widget=DateInput)

    class Meta:
        model = Booking
        fields = ('player_name', 'first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment')

        widgets = {
            #The player name fiel is with a value null, the JavaScript put the value on it, this field is hidden
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'playername', 'type': 'hidden'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'bookdate': forms.DateField(widget=DateInput),
            'timeslot': forms.Select(attrs={'class': 'form-control'}),
            'players': forms.TextInput(attrs={'class': 'form-control'}),
            'tickets': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }



""" 
A VIRER SI LE NOUVEAU MARCHE BIEN

# Form class
class BookingForm(ModelForm):

    # Calendar call
    bookdate = forms.DateField(widget=DateInput)

    class Meta:

        model = Booking

        # Fields required
        fields = ('first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment')
"""
