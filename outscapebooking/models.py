# Import django model
from django.db import models
# Import duser model
from django.contrib.auth.models import User
# Import ValidationError
from django.core.exceptions import ValidationError
# Import date for calendar and date validation
from django.utils.timezone import now
from datetime import date
# Import validators max and min value for players and tickets
from django.core.validators import MaxValueValidator, MinValueValidator
# Import redirection URL
from django.urls import reverse
# Import messaging system
from django.contrib import messages
# Import RegexValidator to validate phone number
from django.core.validators import RegexValidator


"""
Different status for the booking
By default the booking status is 'pending'
"""
STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Declined"))


class Booking(models.Model):
    """
    Database model for booking app
    Every data is save in the database
    """

    def validate_bookdate(value):
        """
        Validate the booking if the booked date is before today
        """
        today = now().date()
        if value <= today:
            raise ValidationError("The date cannot be in the past!")

    """
    List with available timeslots
    """
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
        on_delete=models.CASCADE,
        related_name="booking"
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
        unique=False
        )

    # Mobile number with RegexValidator
    mobile = models.CharField(
        "Your phone number*",
        help_text="[Indicate your country code,  \
            without space. E.g:+336xxxxxxx/+490157xxxxxxxx]",
        max_length=14,
        blank=False,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')]
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

    class Meta:
        # Display the booking list in date descending order
        ordering = ['bookdate']

        # Constraint date and timeslot fields to be unique
        # To avoid double bookings on the same timeslot
        constraints = [
            models.UniqueConstraint(
                fields=['bookdate', 'timeslot'],
                name='unique_booking'
                )
        ]

    # Display the date and timeslot of booking as the title
    def __str__(self):
        return f'Booking on {self.bookdate} {self.timeslot}'

    # Redirection to the booking list when the form is submitted
    def get_absolute_url(self):
        return reverse('booking-list')

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]
