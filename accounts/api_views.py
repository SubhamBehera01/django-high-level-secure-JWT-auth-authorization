# accounts/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
            'roles': [g.name for g in user.groups.all()],
        })
