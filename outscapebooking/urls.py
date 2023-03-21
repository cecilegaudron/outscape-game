from django.urls import path
from . import views
from .views import BookingList, BookingDetailView, AddBookingView



urlpatterns = [
    # URL for Home Page
    path('', views.index, name="index"),
    # IT IS WORKING path('booking.html', views.make_booking, name='booking'),
    path('booking/', AddBookingView.as_view(), name='booking'),
    # URL for Booking List
    path('booking_list', BookingList.as_view(), name='booking-list'),
    # URL for Booking detail called by its Primary Key
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    #path('booking_detail.html/<booking_id>', views.BookingDetailView.as_view(), name='booking-detail'),
    # path('booking_detail.html', views.BookingDetailView.as_view(), name='booking-detail'),
]