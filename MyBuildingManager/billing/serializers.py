from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bill
        fields = '__all__'
        extra_kwargs = {'receipt_photo': {'read_only': True},
                        }
        

class BillUpdateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Bill
        fields = ['receipt_photo' ,]
