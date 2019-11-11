from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime


class Caterer(models.Model):
    caterer_id = models.AutoField(primary_key = True)
    caterer_name = models.CharField(max_length = 100, default="")
    caterer_phone = models.CharField(max_length = 100, default="")
    caterer_email = models.CharField(max_length = 100, default="")
    caterer_menu_type = models.CharField(max_length = 100, default="")
    caterer_menu_cost_per_person = models.CharField(max_length = 100, default="")

    def __str__(self):
        return self.caterer_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key = True)
    customer_first_name = models.CharField(max_length=100, default="")
    customer_last_name = models.CharField(max_length=100, default="")
    customer_street_address = models.CharField(max_length=100, default="")
    customer_city = models.CharField(max_length=100, default="")
    customer_state = models.CharField(max_length=100, default="")
    customer_zip = models.CharField(max_length=5, default="")
    customer_phone = models.CharField(max_length=100, default="")
    customer_email = models.CharField(max_length=100, default="")
    customer_organization = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.customer_first_name + ' ' + self.customer_last_name + ', ' + self.customer_organization


class Venue(models.Model):
    venue_id = models.AutoField(primary_key = True)
    venue_room_name = models.CharField(max_length=100, default="")
    venue_rental_fee = models.CharField(max_length=100, default="")
    venue_room_size = models.BigIntegerField()
    venue_room_capacity = models.BigIntegerField()
    is_booked = models.BooleanField(default='True')

    def __str__(self):
        return self.venue_room_name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key = True)
    caterer = models.ForeignKey(Caterer, related_name = 'bookings', on_delete = models.PROTECT)
    customer = models.ForeignKey(Customer, related_name = 'bookings', on_delete = models.PROTECT)
    venue = models.ForeignKey(Venue, related_name = 'bookings', on_delete = models.PROTECT)
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_start_time = models.DateTimeField(null=True, blank=True)
    booking_end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer)
