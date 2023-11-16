from django.urls import path
from .views import *

urlpatterns = [
    path('register/', ProfileRegisterView.as_view()),
    path('profiles/', ProfileListView.as_view()),
    path('isadmin/', isAdmin),
]