from django.urls import path
from .views import UserCreateView  # Import your views accordingly

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),  # Example registration path
    # Add other authentication-related paths for login, logout, etc.
]
