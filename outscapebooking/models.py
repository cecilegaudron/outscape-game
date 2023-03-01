from django.db import models
from django.contrib.auth.models import User

# Different status for the booking
# By default the booking status is 'pending'

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Declined"))

# Database model for booking app
# Every data is saved in the database
class Booking(models.Model):
    # Username and email are inherit from the user model
    # user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    email = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    # User info
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    mobile = models.CharField(max_length=14, blank=False)
    # Date and hour of booking
    date = models.DateField(blank=False)
    hour = models.TimeField(blank=False)
    # Number of players
    players = models.PositiveIntegerField(blank=False)
    # Number of transport tickets needed for the game
    tickets = models.PositiveIntegerField(blank=True)
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
        ordering = ['-date']
        
        # Constraint date and hour fields to be unique to avoid double bookings on the same timeslot
        constraints = [
            models.UniqueConstraint(fields=['date', 'hour'], name='unique_booking')
        ]

    def __str__(self):
        # Display the date and hour of booking as the title
        return f'Booking on {self.date} {self.hour}'

