# file_upload_app/serializers.py
from rest_framework import serializers
from .models import IndustrialUpload

class IndustrialFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndustrialUpload
        fields = '__all__'  # You can specify the fields to include here if needed
