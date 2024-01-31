# file_upload_app/serializers.py
from rest_framework import serializers
from .models import UploadForms, Feedback, FileUploads


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FileUploadsSerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = FileUploads
        fields = '__all__'

class UploadFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadForms
        fields = '__all__'  # You can specify the fields to include here if needed
