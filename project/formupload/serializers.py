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

    department_type = serializers.SerializerMethodField()
    school_campus = serializers.SerializerMethodField()

    def get_department_type(self, obj):
        if obj.user:
            user = obj.user
            department_type = user.department_type
            return department_type
        return None
    
    def get_school_campus(self, obj):
        if obj.user:
            user = obj.user
            school_campus = user.school_campus
            return school_campus
        return None

    class Meta:
        model = UploadForms
        fields = ['id', 'form_type', 'invention_title', 'summary', 'authors', 'upload_status', 'uploaded_at', 'department_type', 'school_campus'] # You can specify the fields to include here if needed
