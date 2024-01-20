from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework.exceptions import ValidationError
from django.db import models
# from .models import UserProfile
from djoser import utils
from rest_framework.exceptions import ValidationError

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.validators import UniqueValidator  # Add this import


User = get_user_model()

class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            'first_name',
            'last_name',
            'middle_name',
            'user_role',
            'birth_date',
            'is_active',
            'contact_number',
            'school_campus',
            'department_type',
        )
        read_only_fields = (settings.LOGIN_FIELD,)


# registration    
class CustomUserCreateSerializer(UserCreateSerializer):
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    first_name = serializers.CharField(max_length=255, write_only=True)
    last_name = serializers.CharField(max_length=255, write_only=True)
    birth_date = serializers.DateField(input_formats=['%Y-%m-%d'])


    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            'user_role',
            "first_name",
            "middle_name",
            "last_name",
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            'email',
            'contact_number',
            'school_campus',
            'department_type',            
            'birth_date',
        )

    def clean_user_data(self, validated_data):
        return {
            'email' : validated_data.get('email', ''),
            'username' : validated_data.get('username', ''),
            'first_name' : validated_data.get('first_name', ''),
            'middle_name' : validated_data.get('middle_name', ''), 
            'last_name' : validated_data.get('last_name', ''),
            'user_role': validated_data.get('user_role', ''),
            'contact_number': validated_data.get('contact_number', ''),
            'school_campus': validated_data.get('school_campus', ''),
            'department_type': validated_data.get('department_type', ''),
            'birth_date': validated_data.get('birth_date', ''),            
        }


    def validate(self, attrs):
        return attrs
    
    def generate_password(self, last_name, birth_date):
        birthday_string = birth_date.strftime('%Y%m%d')
        default_password = f"{last_name.lower()}@{birthday_string}"
        return default_password



    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        role = validated_data.get("user_role")  # Use validated_data here
        if role == "admin":
            user.is_staff = True
            user.is_superuser = True
            user.save(update_fields=["is_staff", "is_superuser"])

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user_data = self.clean_user_data(validated_data)
            last_name = validated_data.get("last_name", "")
            birth_date = validated_data.get("birth_date", "")
            
            password = self.generate_password(last_name, birth_date)

            user_data["password"] = password

            user = User.objects.create_user(**user_data)

            if settings.SEND_CONFIRMATION_EMAIL:
                user.is_active = True
                user.save(update_fields=["is_active"])

                

        return user





