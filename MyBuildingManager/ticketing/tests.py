from django.test import TestCase
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Announcement,Ticket,TicketStatus
from myauth.models import Profile
from .serializers import AnnouncementSerializer,TicketReplySerializer,TicketSerializer

class AnnouncementListCreateViewTest(APITestCase):
    def setUp(self):
        self.data = {
            'title': 'Test Announcement',
            'description': 'This is a test announcement',
        }
        # Creating a user and token
        user = User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=user, is_admin=True,phone_number=0,house_number=0,floor_number=0)
        token = AccessToken.for_user(user)
        
        # Sending post request with token in headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.response = self.client.post(reverse('announcement-list'), self.data)

    def test_create_announcement(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Announcement.objects.count(), 1)
        self.assertEqual(Announcement.objects.get().title, 'Test Announcement')
        self.assertEqual(Announcement.objects.get().description, 'This is a test announcement')

    def test_get_announcement(self):
        self.response = self.client.get(reverse('announcement-list'))
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data, serializer.data)

class TicketListCreateViewTest(APITestCase):
    def setUp(self):
        self.data = {
            'title': 'Test Ticket',
            'description': 'This is a test ticket',
        }

        # Creating a user and token
        user = User.objects.create_user(username='testuser', password='testpassword')
        Profile.objects.create(user=user, is_admin=True,phone_number=0,house_number=0,floor_number=0)
        token = AccessToken.for_user(user)
        
        # Sending post request with token in headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.response = self.client.post(reverse('ticket-list'), self.data)

    def test_create_ticket(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().title, 'Test Ticket')
        self.assertEqual(Ticket.objects.get().description, 'This is a test ticket')

    def test_get_ticket(self):
        self.response = self.client.get(reverse('ticket-list'))
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data, serializer.data)

        
