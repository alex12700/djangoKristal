from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
from decimal import Decimal

from .models import Room, Room_type, Guest, Booking


User = get_user_model()


class Hotel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='qweasd123456789')
        self.guest = Guest.objects.create(last_name="slave", first_name="fucking", patronimyc=" ", phone=89012345678, email="boys@next.door")
        self.room_type = Room_type.objects.create(room_type="dungeon", beds="3", cost="300", description="get your a$$ back here")
        self.room = Room.objects.create(room_number=6, room_floor=6, status='a', id_room_type=self.room_type)
        self.booking = Booking.objects.create(booking_date=datetime.date(datetime.now()),
                                              checkin_date=datetime.date(datetime.now()),
                                              checkout_date=datetime.date(datetime.now() + timedelta(days=5)),
                                              number_of_nights=5, id_guest=self.guest, id_room=self.room)

    def test_update_room_type(self):
        hello = "hello there"
        self.room_type.description = hello
        self.assertEqual(self.room_type.description, hello)

    # def test_add_work(self):
    #     self.work = WorkModel.objects.create(haircut=self.haircut, client=self.client, master=self.user,
    #                                          date_time=datetime.now())

    def test_change_room_status(self):
        self.assertEqual(self.room.status, 'a')
        self.assertEqual(Booking.objects.filter(booking_date=datetime.date(datetime.now() - timedelta(days=5))).count(), 0)
        # while WorkModel.objects.filter(client=self.client).count() <= 4:
        #     self.test_add_work()
        # self.assertEqual(self.client.status, False)
        self.assertEqual(self.booking.total_cost, int(self.booking.number_of_nights) * int(self.booking.id_room.id_room_type.cost))
        # self.test_add_work()
        self.room.status = 'b'
        satanNumb = 666
        self.booking.number_of_nights = satanNumb
        self.booking.save()
        self.assertEqual(self.room.status, 'b')
        self.assertEqual(self.booking.total_cost, int(self.booking.id_room.id_room_type.cost) * int(satanNumb))



class UsersTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)