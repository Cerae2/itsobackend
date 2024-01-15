from django.urls import path
from .views import TrademarkUploadAPIView

app_name = 'trademark_app'

urlpatterns = [
    path('trademark_upload/', TrademarkUploadAPIView.as_view(), name='trademark_upload'),
    # Add other URLs for different functionalities if needed
]
