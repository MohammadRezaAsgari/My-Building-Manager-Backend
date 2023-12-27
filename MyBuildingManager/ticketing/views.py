from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Ticket, TicketReply, Announcement
from .serializers import TicketSerializer, TicketReplySerializer, AnnouncementSerializer
from myauth.permissions import IsAdmin

# Utility to handle permission logic
def get_custom_permissions(request_method):
    if request_method in ('GET', 'HEAD', 'OPTIONS'):
        return [AllowAny()]
    else:
        return [IsAdmin(), IsAuthenticated()]

# Mixin for common create behavior
class PerformCreateMixin:
    def perform_create(self, serializer):
        user_profile = get_object_or_404(Profile, user_id=self.request.user.id)
        serializer.save(author=user_profile)

# Tickets APIs ---------------------------------------------------------------------
class TicketListCreateView(PerformCreateMixin, generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TicketRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
# ----------------------------------------------------------------------------------

# Replies APIs ---------------------------------------------------------------------
class ReplyListCreateView(PerformCreateMixin, generics.ListCreateAPIView):
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer

    def get_permissions(self):
        return get_custom_permissions(self.request.method)

class ReplyRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TicketReply.objects.all()
    serializer_class = TicketReplySerializer
# ----------------------------------------------------------------------------------

# Announcement APIs ----------------------------------------------------------------
class AnnouncementListCreateView(PerformCreateMixin, generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get_permissions(self):
        return get_custom_permissions(self.request.method)

class AnnouncementRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
# ----------------------------------------------------------------------------------
