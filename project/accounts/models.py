from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    # Constants for user roles
    USER_ROLE_CHOICES = [
        ('researcher', 'Researcher'),
        ('admin', 'Admin'),
    ]

    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=12, blank=True) 
    school_campus = models.CharField(max_length=50, null=True, blank=True)
    department_type = models.CharField(max_length=50, null=True, blank=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='admin')


    def __str__(self):
        return f'{self.username}'