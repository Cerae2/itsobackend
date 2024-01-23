from .models import UploadForms
from .serializers import UploadFormSerializers
from rest_framework import generics

class UploadFormAPIView(generics.CreateAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers