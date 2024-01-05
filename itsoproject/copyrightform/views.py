# views.py (file_upload_app/views.py)
from rest_framework import generics
from .models import CopyrightUpload
from .serializers import CopyrightFileSerializers

class CopyrightUploadAPIView(generics.ListCreateAPIView):
    queryset = CopyrightUpload.objects.all()
    serializer_class = CopyrightFileSerializers
