from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomUserCreateView

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),  # Login endpoint
    path('register/', CustomUserCreateView.as_view(), name='register'),  # Register endpoint
]
