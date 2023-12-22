from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from .models import Profile


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=50)
    last_name = serializers.CharField(required=True, max_length=50)
    username = serializers.CharField(required=True,max_length=50)
    password = serializers.CharField(
        write_only=True,
        required=True,
        max_length=50,
    )

    phone_number = serializers.CharField(required=True, max_length=50)
    house_number = serializers.IntegerField()
    floor_number = serializers.IntegerField()
    is_admin = serializers.BooleanField(required=False,default=False)
    
    def validate(self, attrs):
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError("This username already exists!")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        Profile.objects.create(
            user=user,
            phone_number=validated_data["phone_number"],
            house_number=validated_data["house_number"],
            floor_number=validated_data["floor_number"],
            is_admin=validated_data["is_admin"]
        )
        return self.validated_data

class UserSerializer(serializers.ModelSerializer):

    class Meta: 
        model = User
        fields = ['first_name','last_name','username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta: 
        model = Profile
        fields = '__all__'
