from rest_framework import serializers
from .models import IndustrialFile

class IndustrialFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndustrialFile
        fields = '__all__'
