from rest_framework import serializers
from .models import Ticket, TicketReply, Announcement
from myauth.serializers import ProfileSerializer

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id',
            'author',
            'title',
            'description',
            'created_at',
            'status',
            )
        
        extra_kwargs = {
            'author': {
            'read_only': True,
            },
        }


class TicketReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketReply
        fields = ('id',
                  'parent_ticket',
                  'description',
                  'created_at')



class AnnouncementSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    class Meta:
        model = Announcement
        fields = (
            'id',
            'author',
            'title',
            'description',
            'created_at',
            )
        