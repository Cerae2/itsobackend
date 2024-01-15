from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class User(AbstractUser):
    COLLEGE_CHOICES = [
        ('engineering_architecture', 'College of Engineering and Architecture'),
        ('information_technology', 'College of Information Technology and Computing'),
        ('science_mathematics', 'College of Science and Mathematics'),
        ('science_tech_education', 'College of Science and Technology Education'),
        ('technology', 'College of Technology'),
        ('medicine', 'College of Medicine'),
        ('senior_high_school', 'Senior High School'),
    ]
    
    # Constants for user roles
    USER_ROLE_CHOICES = [
        ('client', 'Client'),
        ('employee', 'Employee'),
        ('admin', 'Admin'),
    ]

    # Constants for school campuses
    SCHOOL_CAMPUS_CHOICES = [
        ('ustp_alubijid', 'USTP Alubijid'),
        ('ustp_cagayan_de_oro', 'USTP Cagayan de Oro'),
        ('ustp_claveria', 'USTP Claveria'),
        ('ustp_balubal', 'USTP Balubal'),
        ('ustp_jasaan', 'USTP Jasaan'),
        ('ustp_oroquieta', 'USTP Oroquieta'),
        ('ustp_panaon', 'USTP Panaon'),
        ('ustp_villanueva', 'USTP Villanueva'),
    ]

    middle_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=12, blank=True)  # Allow blank
    school_campus = models.CharField(max_length=50, choices=SCHOOL_CAMPUS_CHOICES, default='ustp_cagayan_de_oro')
    department_type = models.CharField(max_length=50, choices=COLLEGE_CHOICES, default='information_technology')
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='admin')