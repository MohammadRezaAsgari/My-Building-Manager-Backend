from django.urls import path
from .views import *

urlpatterns = [
    path('tickets/', TicketListView.as_view()),
    path('tickets/create/', TicketCreateView.as_view()),
    path('tickets/<int:pk>', TicketRetrieveUpdateView.as_view()),

    path('tickets/replies/', ReplyListView.as_view()),
    path('tickets/replies/create/', ReplyCreateView.as_view()),
    path('tickets/replies/<int:pk>', ReplyRetrieveUpdateView.as_view()),

    path('announcements/', AnnouncementListView.as_view()),
    path('announcements/create/', AnnouncementCreateView.as_view()),
    path('announcements/<int:pk>', AnnouncementRetrieveUpdateView.as_view()),
]