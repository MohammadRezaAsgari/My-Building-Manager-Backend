from django.contrib import admin
from .models import Ticket,TicketReply, Announcement

admin.site.register(Announcement)
admin.site.register(Ticket)
admin.site.register(TicketReply)
