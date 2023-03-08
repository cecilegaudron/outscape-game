from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking
from .admin import BookingAdmin


class MyTestCase(TestCase):
    """
    Tests for the booking app
    def test_status(self):
        reservation = Booking.objects.create(
            email='incognito@gmail.com',
            mobile='015748965205',
            date='2023-05-01',
            timeslot='10:00-13:00',
            players='5',
            tickets='2',
            comment='with a baby'
        )
        

        self.assertEqual(reservation.status, 0)
    """