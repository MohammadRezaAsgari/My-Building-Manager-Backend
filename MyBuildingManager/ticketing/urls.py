from django.urls import path
from .views import *

urlpatterns = [
    path('tickets/', TicketListCreateView.as_view(),name='ticket-list'),
    path('tickets/<int:pk>', TicketRetrieveUpdateView.as_view()),

    path('replies/', ReplyListCreateView.as_view(),name='reply-list'),
    path('replies/<int:pk>', ReplyRetrieveUpdateView.as_view()),

    path('announcements/', AnnouncementListCreateView.as_view(),name='announcement-list'),
    path('announcements/<int:pk>', AnnouncementRetrieveUpdateView.as_view()),
]