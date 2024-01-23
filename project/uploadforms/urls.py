from django.urls import path
from .views import UploadFormAPIView

app_name = 'upload_app'

urlpatterns = [
    path('', UploadFormAPIView.as_view(), name='upload_form'),
    # Add other URLs for different functionalities if needed
]
