from . import views
from django.urls import path
from .views import BookingList, make_booking, MyBooking



urlpatterns = [
    path('', views.BookingList.as_view(), name='index'),
    path('booking.html', views.make_booking, name='booking'),
    path('booking_list.html', views.BookingList.as_view(), name='booking-list'),
    path('booking_detail.html', views.MyBooking.as_view(), name='booking-detail'),
]