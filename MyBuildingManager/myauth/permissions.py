from rest_framework.permissions import BasePermission
from .models import Profile


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            profile = Profile.objects.get(user_id=request.user.id)
            return profile.is_admin

        return False

