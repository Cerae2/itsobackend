from django.urls import path
from .views import UtilityUploadAPIView

app_name = 'utility_app'

urlpatterns = [
    path('utility_upload/', UtilityUploadAPIView.as_view(), name='utility_upload'),
    # Add other URLs for different functionalities if needed
]
