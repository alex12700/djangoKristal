from django.db import models

class Guest(models.Model):
    id_guest = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronimyc = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Room_type(models.Model):
    id_room_type = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=50)
    beds = models.CharField(max_length=50)
    cost = models.IntegerField()
    description = models.CharField(max_length=500)

class Room(models.Model):
    id_room = models.IntegerField(primary_key=True)
    room_number = models.IntegerField()
    room_floor = models.IntegerField()
    status = models.CharField(max_length=50)
    id_room_type = models.ForeignKey(Guest, on_delete=models.CASCADE)

class Booking(models.Model):
    id_booking = models.IntegerField(primary_key=True)
    booking_date = models.DateTimeField()
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    guest_number = models.IntegerField()
    number_of_nights = models.IntegerField()
    id_employee = models.ForeignKey(Guest, on_delete=models.CASCADE)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)



