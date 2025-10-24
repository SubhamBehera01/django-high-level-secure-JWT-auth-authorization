# accounts/urls.py
from django.urls import path
from .views import MyTokenObtainPairView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
from . import api_views

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    # Example of protected endpoint
    path('profile/', api_views.ProfileView.as_view(), name='profile'),
]
