from rest_framework import serializers
from .models import FeedbackstatusAPI

class FeedbackstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackstatusAPI   
        fields = '__all__'