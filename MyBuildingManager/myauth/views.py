from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsAdmin
from django.http import JsonResponse
from rest_framework import generics
from .models import Profile
from .serializers import RegisterSerializer, ProfileSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def isAdmin(request: Request):
    return JsonResponse({"isadmin": Profile.objects.get(user_id=request.user.id).is_admin})

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.filter(is_admin=False)
    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin, IsAuthenticated]

    
class ProfileRegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]