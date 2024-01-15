# file_upload_app/serializers.py
from rest_framework import serializers
from .models import UtilityUpload

class UtilityFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UtilityUpload
        fields = '__all__'  # You can specify the fields to include here if needed
