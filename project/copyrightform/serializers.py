# file_upload_app/serializers.py
from rest_framework import serializers
from .models import CopyrightUpload

class CopyrightFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = CopyrightUpload
        fields = '__all__'  # You can specify the fields to include here if needed
