from rest_framework import serializers
from .models import Ticket, Announcement
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
            'reply_description',
            )
        
        extra_kwargs = {
            'author': {
            'read_only': True,
            },
        }


class TicketReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
                  'reply_description',)



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
        