# views.py (file_upload_app/views.py)
from rest_framework import generics
from .models import UtilityUpload
from .serializers import UtilityFileSerializers

class UtilityUploadAPIView(generics.ListCreateAPIView):
    queryset = UtilityUpload.objects.all()
    serializer_class = UtilityFileSerializers
