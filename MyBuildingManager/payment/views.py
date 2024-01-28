from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Card
from billing.models import Bill
from .serializers import CardSerializer

class PayBillApiView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request, pk):
        try:
            bill = Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        price = bill.calculate_total()
        
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():

            
            
            card_number = serializer.validated_data.get('card_number')
            password = serializer.validated_data.get('password')
            try:
                card = Card.objects.get(card_number=card_number, password=password)
            except Card.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            if card.balance>price:
                card.balance -= price
                card.save()
                bill.payment_status = True
                bill.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(CardSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(CardSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
