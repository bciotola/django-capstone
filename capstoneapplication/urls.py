"""capstone_production URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from capstoneapplication.views import (
    CatererList,
    CustomerList,
    VenueList,
    BookingList,
    CatererDetail,
    CustomerDetail,
    VenueDetail,
    BookingDetail,
)

urlpatterns = [
    path('caterer/',
         CatererList.as_view(),
         name='capstoneapplication_caterer_list_urlpattern'),

    path('caterer/<int:pk>/',
         CatererDetail.as_view(),
         name='capstoneapplication_caterer_detail_urlpattern'),

    path('customer/',
         CustomerList.as_view(),
         name='capstoneapplication_customer_list_urlpattern'),

    path('customer/<int:pk>/',
         CustomerDetail.as_view(),
         name='capstoneapplication_customer_detail_urlpattern'),

    path('venue/', VenueList.as_view(),
         name='capstoneapplication_venue_list_urlpattern'),

    path('venue/<int:pk>/',
         VenueDetail.as_view(),
         name='capstoneapplication_venue_detail_urlpattern'),

    path('booking/', BookingList.as_view(),
         name='capstoneapplication_booking_list_urlpattern'),

    path('booking/<int:pk>/',
         BookingDetail.as_view(),
         name='capstoneapplication_booking_detail_urlpattern'),
    ]
