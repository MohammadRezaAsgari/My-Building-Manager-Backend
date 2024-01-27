from django.contrib import admin
from .models import Ticket, Announcement

admin.site.register(Announcement)
admin.site.register(Ticket)
