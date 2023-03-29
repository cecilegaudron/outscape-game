from django import forms
from .models import Booking
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.forms.fields import DateField


# Creation of custom widget for a calendar
class DateInput(forms.DateInput):
    input_type = 'date'


# Choose which fields are display to the user
class BookingForm(forms.ModelForm):

    bookdate = forms.DateField(widget=DateInput)

    class Meta:
        model = Booking
        fields = (
            'player_name',
            'first_name',
            'last_name',
            'email',
            'mobile',
            'bookdate',
            'timeslot',
            'players',
            'tickets',
            'comment'
            )

        widgets = {
            # Player name field is a value null
            # JavaScript put the value on it, this field is hidden
            'player_name': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'playername',
                'type': 'hidden'
                }),
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
