from .models import UploadForms
from .serializers import UploadFormSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class UploadFormAPIView(generics.CreateAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers


class CustomFileListView(generics.ListAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        return queryset.filter(user = self.request.user.id)