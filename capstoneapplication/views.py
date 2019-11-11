from django.shortcuts import render, get_object_or_404, render_to_response
from django.http.response import HttpResponse
from django.template import loader
from django.views import View

from .models import (
    Caterer,
    Customer,
    Venue,
    Booking,
)

# FUNCTION BASED VIEW
# def caterer_list_view(request):
#     caterer_list = Caterer.objects.all()
#     # caterer_list = Caterer.objects.none()
#     template = loader.get_template(
#         'capstoneapplication/caterer_list.html')
#     context = {'caterer_list': caterer_list}
#     output = template.render(context)
#     return HttpResponse(output)


#CLASS BASED VIEW
class CatererList(View):

	def get(self, request):
		return render(
			request,
			'capstoneapplication/caterer_list.html',
			{'caterer_list': Caterer.objects.all()}
			)


class CatererDetail(View):

    def get(self, request, pk):
        caterer = get_object_or_404(
            Caterer,
            pk=pk
        )
        booking_list = caterer.bookings.all()
        return render_to_response(
            'capstoneapplication/caterer_detail.html',
            {'caterer': caterer, 'booking_list': booking_list}
        )
# def customer_list_view(request):
#     customer_list = Customer.objects.all()
#     # customer_list = Customer.objects.none()
#     template = loader.get_template(
#         'capstoneapplication/customer_list.html')
#     context = {'customer_list': customer_list}
#     output = template.render(context)
#     return HttpResponse(output)


class CustomerList(View):

    def get(self, request):
        return render(
            request,
            'capstoneapplication/customer_list.html',
            {'customer_list': Customer.objects.all()}
        )


class CustomerDetail(View):

    def get(self, request, pk):
        customer = get_object_or_404(
            Customer,
            pk=pk
        )
        booking_list = customer.bookings.all()
        return render_to_response(
            'capstoneapplication/customer_detail.html',
            {'customer': customer, 'booking_list': booking_list}
        )
# def venue_list_view(request):
#     venue_list = Venue.objects.all()
#     # venue_list = Venue.objects.none()
#     template = loader.get_template(
#         'capstoneapplication/venue_list.html')
#     context = {'venue_list': venue_list}
#     output = template.render(context)
#     return HttpResponse(output)


class VenueList(View):

    def get(self, request):
        return render(
            request,
            'capstoneapplication/venue_list.html',
            {'venue_list': Venue.objects.all()}
        )


class VenueDetail(View):

    def get(self, request, pk):
        venue = get_object_or_404(
            Venue,
            pk=pk
        )
        booking_list = venue.bookings.all()
        return render_to_response(
            'capstoneapplication/venue_detail.html',
            {'venue': venue, 'booking_list': booking_list}
        )
# def booking_list_view(request):
#     booking_list = Booking.objects.all()
#     # booking_list = Booking.objects.none()
#     template = loader.get_template(
#         'capstoneapplication/booking_list.html')
#     context = {'booking_list': booking_list}
#     output = template.render(context)
#     return HttpResponse(output)


class BookingList(View):

    def get(self, request):
        return render(
            request,
            'capstoneapplication/booking_list.html',
            {'booking_list': Booking.objects.all()}
        )


class BookingDetail(View):

    def get(self, request, pk):
        booking = get_object_or_404(
            Booking,
            pk=pk
        )
        venue = booking.venue
        customer = booking.customer
        caterer = booking.caterer
        return render_to_response(
            'capstoneapplication/booking_detail.html',
            {'booking': booking,
             'venue': venue,
             'customer': customer,
             'caterer': caterer}
        )