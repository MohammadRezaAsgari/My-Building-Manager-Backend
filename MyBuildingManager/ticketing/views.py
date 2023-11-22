from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from rest_framework import generics
from .models import Ticket,TicketReply, Announcement
from .serializers import TicketSerializer,TicketReplySerializer, AnnouncementSerializer
from myauth.permissions import IsAdmin
from myauth.models import Profile

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
NOT_SAFE_METHODS = ('POST', 'PUT', 'PATCH','DELETE')

#Tickets APIs ---------------------------------------------------------------------
class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        try:
            serializer.save(author=Profile.objects.get(user_id=self.request.user.id))
        except:
            return
        

class TicketRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
#----------------------------------------------------------------------------------


#Replies APIs ---------------------------------------------------------------------
class ReplyListCreateView(generics.ListCreateAPIView):
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer
    permission_classes = [AllowAny,IsAdmin, IsAuthenticated ]

    def perform_create(self, serializer):
        try:
            reply = serializer.save()
            TicketReply.update(id=reply.parent_ticket.id)
        except:
            return
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny(),]
        elif self.request.method in NOT_SAFE_METHODS:
            return  [IsAdmin(), IsAuthenticated() ]

class ReplyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer
#----------------------------------------------------------------------------------


#Announcement APIs ----------------------------------------------------------------
class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        serializer.save(author=Profile.objects.get(user_id=self.request.user.id))

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny(),]
        elif self.request.method in NOT_SAFE_METHODS:
            return  [IsAdmin(), IsAuthenticated() ]

class AnnouncementRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
#----------------------------------------------------------------------------------
