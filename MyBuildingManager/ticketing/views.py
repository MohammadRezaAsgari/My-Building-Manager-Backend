from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework import generics
from .models import Ticket,TicketReply, Announcement
from .serializers import TicketSerializer,TicketReplySerializer, AnnouncementSerializer
from myauth.permissions import IsAdmin
from myauth.models import Profile

#Tickets APIs ---------------------------------------------------------------------
class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny, ]

class TicketCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        serializer.save(author=Profile.objects.get(user_id=self.request.user.id))

class TicketRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
#----------------------------------------------------------------------------------


#Replies APIs ---------------------------------------------------------------------
class ReplyListView(generics.ListAPIView):
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer
    permission_classes = [AllowAny, ]

class ReplyCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin, IsAuthenticated]
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer

    def perform_create(self, serializer):
        reply = serializer.save()
        TicketReply.update(id=reply.parent_ticket.id)

class ReplyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer
#----------------------------------------------------------------------------------


#Announcement APIs ----------------------------------------------------------------
class AnnouncementListView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [AllowAny, ]

class AnnouncementCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(author=Profile.objects.get(user_id=self.request.user.id))

class AnnouncementRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
#----------------------------------------------------------------------------------
