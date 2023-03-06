from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking
from .admin import BookingAdmin

# Create your tests here.

class MyTestCase(TestCase):
    def test_admin_methods(self):
        test_user = User.objects.create(
            username='Jane',
            first_name='Janette',
            last_name='Doe',
            password='password',
            email='janedoe@gmail.com',
        )