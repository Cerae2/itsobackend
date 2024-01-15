# file_upload_app/serializers.py
from rest_framework import serializers
from .models import TrademarkUpload

class TrademarkFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrademarkUpload
        fields = '__all__'  # You can specify the fields to include here if needed
