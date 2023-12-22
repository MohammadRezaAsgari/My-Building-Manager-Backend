from django.shortcuts import render
from rest_framework import generics
from .models import Bill
from myauth.models import Profile
from .serializers import BillSerializer ,BillUpdateSerializer
from myauth.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
NOT_SAFE_METHODS = ('POST', 'PUT', 'PATCH','DELETE')

class BillsListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAdmin,]

class BillsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAdmin,]


class UserBillsListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.filter(user=Profile.objects.get(user_id=self.request.user.id).id)
    

class UserBillsRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.filter(user=Profile.objects.get(user_id=self.request.user.id).id)
    
    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return BillSerializer
        elif self.request.method in NOT_SAFE_METHODS:
            return  BillUpdateSerializer

