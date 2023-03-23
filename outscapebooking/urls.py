from django.urls import path
from . import views
from .views import BookingList, BookingDetailView, AddBookingView, UpdateBookingView, DeleteBookingView, PastBookingList


urlpatterns = [
    # URLs for info pages
    path('', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('game.html', views.game, name="game"),

    # URL for Booking form
    path('booking/', AddBookingView.as_view(), name='booking'),

    # URL for Booking list
    path('booking_list', BookingList.as_view(), name='booking-list'),

    # URL for Booking detail called by its Primary Key
    path('booking/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),

    # URL for Booking update
    path('booking/update/<int:pk>/', UpdateBookingView.as_view(), name='booking-update'),

    # URL for Booking delete
    path('booking/<int:pk>/delete', DeleteBookingView.as_view(), name='booking-delete'),

    # URL for Past Booking List
    path('booking_past', PastBookingList.as_view(), name='booking-past'),
]