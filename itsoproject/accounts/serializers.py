from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'birth_date', 'contact_number', 'school_campus', 'department_type', 'user_role')
        extra_kwargs = {'password': {'write_only': True}}  # Ensures password field is write-only
