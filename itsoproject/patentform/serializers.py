# file_upload_app/serializers.py
from rest_framework import serializers
from .models import PatentUpload

class PatentFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatentUpload
        fields = '__all__'  # You can specify the fields to include here if needed
