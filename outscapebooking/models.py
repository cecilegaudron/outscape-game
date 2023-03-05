from django.db import models
from django.contrib.auth.models import User

# Different status for the booking
# By default the booking status is 'pending'

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Declined"))

""" Database model for booking app 
Every data is save in the database
Follow the course of CI and this page https://docs.djangoproject.com/fr/4.1/topics/db/models/
"""
class Booking(models.Model):

    # List with available timeslots
    # https://stackoverflow.com/questions/64225732/how-to-get-time-slot-in-django-for-doctor-appointment
    TIMESLOT_LIST = (
        (0, '10:00-13:00'),
        (1, '11:00-14:00'),
        (2, '12:00-15:00'),
        (3, '13:00-16:00'),
        (4, '14:00-17:00'),
        (5, '15:00-18:00'),
        (6, '16:00-19:00'),
    )

    # User info
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False, unique=True)
    mobile = models.CharField(max_length=14, blank=False)

    # Date and hour of booking
    date = models.DateField(help_text="DD-MM-YYYY", blank=False)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST, blank=False, null=False)
    hour = models.TimeField(blank=False)

    # Number of players
    players = models.PositiveIntegerField(blank=False)

    # Number of transport tickets needed for the game
    tickets = models.IntegerField("BVG tickets needed", blank=True, null=True)

    # Comment from the customer
    comment = models.TextField(max_length=300, blank=True)

    # Date of the booking creation
    created_on = models.DateTimeField(auto_now_add=True)

    # status of the booking by default it is 'pending'
    status = models.IntegerField(choices=STATUS, default=0)


    class Meta:
        # Name the database
        db_table = 'bookings'

        # Display the booking list in date descending order
        ordering = ['date']
        
        # Constraint date and hour fields to be unique to avoid double bookings on the same timeslot
        constraints = [
            models.UniqueConstraint(fields=['date', 'hour'], name='unique_booking')
        ]


    def __str__(self):
        # Display the date and hour of booking as the title
        return f'Booking on {self.date} {self.hour}'


    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

