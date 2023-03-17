from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

# Different status for the booking
# By default the booking status is 'pending'

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Declined"))

""" Database model for booking app 
Every data is save in the database
Follow the course of CI and this page https://docs.djangoproject.com/fr/4.1/topics/db/models/
"""
class Booking(models.Model):

    def validate_bookdate(value):
        # Validate the booking if the booked date is before today
        # https://stackoverflow.com/questions/66882721/how-to-add-todays-date-to-django-templates
        # https://stackoverflow.com/questions/50439356/django-date-validation-help-needed
        # https://docs.djangoproject.com/en/4.1/ref/validators/
        # Help in Slack
        today = now().date()
        if value <= today:
            raise ValidationError("The date cannot be in the past!")

    # List with available timeslots
    # https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78
    TIMESLOT_LIST = (
        ("10:00-13:00", "10:00-13:00"),
        ("11:00-14:00", "11:00-14:00"),
        ("12:00-15:00", "12:00-15:00"),
        ("13:00-16:00", "13:00-16:00"),
        ("14:00-17:00", "14:00-17:00"),
        ("15:00-18:00", "15:00-18:00"),
        ("16:00-19:00", "16:00-19:00"),
    )

    # User info
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False, unique=True)
    # https://docs.djangoproject.com/en/2.2/ref/validators/
    mobile = models.CharField(max_length=14, blank=False)

    # Date and timeslots of booking
    bookdate = models.DateField(help_text="DD-MM-YYYY", blank=False, validators=[validate_bookdate])
    #date = models.DateField(help_text="DD-MM-YYYY", blank=False, validators=[validate_bookdate])
    timeslot = models.CharField(choices=TIMESLOT_LIST, blank=False, null=False, max_length=40)

    # Number of players
    # https://stackoverflow.com/questions/42425933/how-do-i-set-a-default-max-and-min-value-for-an-integerfield-django
    players = models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1), MaxValueValidator(10)])

    # Number of transport tickets needed for the game
    tickets = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(10)])

    # Comment from the customer
    comment = models.TextField(max_length=300, blank=True)

    # Date of the booking creation
    created_on = models.DateTimeField(auto_now_add=True)

    # status of the booking by default it is 'pending'
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        
        # Display the booking list in date descending order
        ordering = ['bookdate']
        
        # Constraint date and timeslot fields to be unique to avoid double bookings on the same timeslot
        constraints = [
            models.UniqueConstraint(fields=['bookdate', 'timeslot'], name='unique_booking')
        ]

    def __str__(self):
        # Display the date and timeslot of booking as the title
        return f'Booking on {self.bookdate} {self.timeslot}'

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]