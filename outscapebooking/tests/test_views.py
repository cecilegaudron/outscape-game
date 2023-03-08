from django.test import TestCase
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import TemplateView
from .views import BookingList


class ViewsTest(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='jhgdfhgfgh')
        test_user2 = User.objects.create_user(username='testuser2', password='gfdgfdskudjhh')

        test_user1.save()
        test_user2.save()

        # Create a booking
        test_booking = Booking.objects.create(
            email='incognito@gmail.com',
            mobile='015748965205',
            date='2023-05-01',
            timeslot='10:00-13:00',
            players='5',
            tickets='2',
            comment='with a baby'
        )

        def test_redirect_if_not_logged_in(self):
            response = self.client.get(reverse('index.html'))
            self.assertRedirects(response, '/accounts/login/?next=/index.html/')

        def test_logged_in_uses_correct_template(self):
            login = self.client.login(username='testuser1', password='jhgdfhgfgh')
            response = self.client.get(reverse('index.html'))

            # Check our user is logged in
            self.assertEqual(str(response.context['user']), 'testuser1')
            # Check that we got a response "success"
            self.assertEqual(response.status_code, 200)
