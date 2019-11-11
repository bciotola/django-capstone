from django.contrib import admin
from . import models
from .models import Customer
from .models import Venue
from .models import Booking


# Register your models here.
admin.site.register(models.Caterer)
admin.site.register(Customer)
admin.site.register(Venue)
admin.site.register(Booking)
