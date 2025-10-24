# accounts/permissions.py
from rest_framework.permissions import BasePermission

class IsInGroup(BasePermission):
    required_group = None

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return user.groups.filter(name=self.required_group).exists()

# inside view
from .permissions import IsInGroup


