# views.py (file_upload_app/views.py)
from rest_framework import generics
from .models import PatentUpload
from .serializers import PatentFileSerializers

class PatentUploadAPIView(generics.ListCreateAPIView):
    queryset = PatentUpload.objects.all()
    serializer_class = PatentFileSerializers
