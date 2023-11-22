from django.urls import path
from .views import *

urlpatterns = [
    path('tickets/', TicketListCreateView.as_view()),
    path('tickets/<int:pk>', TicketRetrieveUpdateView.as_view()),

    path('replies/', ReplyListCreateView.as_view()),
    path('replies/<int:pk>', ReplyRetrieveUpdateView.as_view()),

    path('announcements/', AnnouncementListCreateView.as_view()),
    path('announcements/<int:pk>', AnnouncementRetrieveUpdateView.as_view()),
]