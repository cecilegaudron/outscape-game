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

    # User model
    player_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )

    # User info with whole name
    first_name = models.CharField(
        "Your first name*",
        max_length=80,
        blank=False
        )

    last_name = models.CharField(
        "Your last name*",
        max_length=80,
        blank=False
        )

    # Email
    email = models.EmailField(
        "Your email address*", 
        blank=False,
        unique=True
        )

    # Mobile number
    # https://docs.djangoproject.com/en/2.2/ref/validators/
    mobile = models.CharField(
        "Your phone number*", 
        help_text="[Indicate your country code]",
        max_length=14,
        blank=False,
        )

    # Date
    bookdate = models.DateField(
        "The booking date*",
        help_text="[It is not possible to book the current day]",
        blank=False,
        validators=[validate_bookdate]
        )
    
    # Timeslots
    timeslot = models.CharField(
        "Choose your time slot*",
        help_text="[The game lasts for the duration of the slot]",
        choices=TIMESLOT_LIST,
        blank=False,
        null=False,
        max_length=40
        )

    # Number of players
    # https://stackoverflow.com/questions/42425933/how-do-i-set-a-default-max-and-min-value-for-an-integerfield-django
    players = models.PositiveIntegerField(
        "Number of players*",
        help_text="[You can't reserve for more than 10 players]",
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(10)]
        )

    # Number of transport tickets needed for the game
    tickets = models.PositiveIntegerField(
        "Number of public transport tickets",
        blank=True,
        null=True,
        validators=[MaxValueValidator(10)]
        )

    # Comment from the customer
    comment = models.TextField(
        "Your comment",
        max_length=300,
        blank=True
        )

    # Date of the booking creation
    created_on = models.DateTimeField(auto_now_add=True)

    # Status of the booking by default it is 'pending'
    status = models.IntegerField(choices=STATUS, default=0)

    # Reservation ID
    booking_id = models.AutoField(auto_created=True, primary_key=True)

    # Slug
    #slug = models.SlugField(max_length=100, unique=True)

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