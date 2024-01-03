from rest_framework import serializers
from .models import UtilityFile

class UtilityFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UtilityFile
        fields = '__all__'
