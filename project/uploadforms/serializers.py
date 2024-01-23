# file_upload_app/serializers.py
from rest_framework import serializers
from .models import UploadForms

class UploadFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadForms
        fields = '__all__'  # You can specify the fields to include here if needed
