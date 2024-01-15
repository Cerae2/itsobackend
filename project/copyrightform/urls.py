from django.urls import path
from .views import CopyrightUploadAPIView

app_name = 'copyright_app'

urlpatterns = [
    path('copyright_upload/', CopyrightUploadAPIView.as_view(), name='copyright_upload'),
    # Add other URLs for different functionalities if needed
]
