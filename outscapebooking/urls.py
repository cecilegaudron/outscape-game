from . import views
from django.urls import path
from .views import BookingList, BookingForm



urlpatterns = [
    path('', views.BookingList.as_view(), name='index'),
    path('booking.html', views.make_booking, name='booking'),
]