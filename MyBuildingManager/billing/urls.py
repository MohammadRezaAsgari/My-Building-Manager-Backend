from django.urls import path
from .views import *
from payment.views import PayBillApiView
urlpatterns = [
    path('bills/', BillsListCreateView.as_view()),
    path('bills/<int:pk>', BillsRetrieveUpdateDestroyView.as_view()),
    path('bills/<int:pk>/payment/', PayBillApiView.as_view()),
    path('user/bills/', UserBillsListView.as_view()),
    path('user/bills/<int:pk>', UserBillsRetrieveUpdateView.as_view()),

]