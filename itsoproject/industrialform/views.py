# views.py (file_upload_app/views.py)
from rest_framework import generics
from .models import IndustrialUpload
from .serializers import IndustrialFileSerializers

class IndustrialUploadAPIView(generics.ListCreateAPIView):
    queryset = IndustrialUpload.objects.all()
    serializer_class = IndustrialFileSerializers
