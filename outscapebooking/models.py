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
    mobile = models.CharField(max_length=14, blank=False)

    # Date and timeslots of booking
    date = models.DateField(help_text="DD-MM-YYYY", blank=False)
    timeslot = models.CharField(choices=TIMESLOT_LIST, blank=False, null=False, max_length=40)

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
        
        # Display the booking list in date descending order
        ordering = ['date']
        
        # Constraint date and timeslot fields to be unique to avoid double bookings on the same timeslot
        constraints = [
            models.UniqueConstraint(fields=['date', 'timeslot'], name='unique_booking')
        ]


    def __str__(self):
        # Display the date and timeslot of booking as the title
        return f'Booking on {self.date} {self.timeslot}'


    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]