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

    """
    first_name = forms.CharField(
        label='Your first name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your first name'}),
    )

    last_name = forms.CharField(
        label='Your last name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your last name'}),
    )

    email = forms.EmailField(
        label='Your email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your address email'}),
    )

    mobile = forms.CharField(
        label='Your telephone number',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Your phone number with country code'}),    
    )

    bookingdate = forms.DateField(
        label='',
        required=True,
        validators=[Booking.validate_bookdate],   
    )

    timeslot = forms.MultipleChoiceField(
        label='Contact Number',
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=TIMESLOT_LIST,
    )

    players = forms.IntegerField(
        label='Number of players',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'How many players are you?'}),
        validators=[MinValueValidator(1), MaxValueValidator(10)],  
    )

    tickets = forms.IntegerField(
        label='Number of public transport tickets ',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Do you need BVG tickets?'}),
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )

    comment = forms.CharField(
        label='Comment',
        required=False,
        max_length=300,
        widget=forms.Textarea(attrs={'placeholder': 'Would you like to inform us of anything in particular?'}),
    )
    """

    class Meta:

        model = Booking

        # Fields required
        fields = ('first_name', 'last_name', 'email', 'mobile', 'bookdate', 'timeslot', 'players', 'tickets', 'comment')