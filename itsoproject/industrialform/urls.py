from django.urls import path
from .views import IndustrialUploadAPIView

app_name = 'industrial_app'

urlpatterns = [
    path('industrial_upload/', IndustrialUploadAPIView.as_view(), name='industrial_upload'),
    # Add other URLs for different functionalities if needed
]
