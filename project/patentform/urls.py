from django.urls import path
from .views import PatentUploadAPIView

app_name = 'patent_app'

urlpatterns = [
    path('patent_upload/', PatentUploadAPIView.as_view(), name='patent_upload'),
    # Add other URLs for different functionalities if needed
]
