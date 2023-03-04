from django.urls import path
from .views import BookingList, BookingView


urlpatterns = [
    #path('', views.BookingList.as_view(), name='index')
    path('', BookingView.as_view(), name='index'), 
]