# views.py (file_upload_app/views.py)
from rest_framework import generics
from .models import TrademarkUpload
from .serializers import TrademarkFileSerializers

class TrademarkUploadAPIView(generics.ListCreateAPIView):
    queryset = TrademarkUpload.objects.all()
    serializer_class = TrademarkFileSerializers
