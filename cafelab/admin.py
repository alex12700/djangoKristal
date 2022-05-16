from django.contrib import admin

from .models import Guest, Room, Room_type, Booking

admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Room_type)
admin.site.register(Booking)