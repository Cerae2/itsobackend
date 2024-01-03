from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# class CustomUser(AbstractUser):
#     # Constants for different colleges and schools
#     COLLEGE_CHOICES = [
#         ('engineering_architecture', 'College of Engineering and Architecture'),
#         ('information_technology', 'College of Information Technology and Computing'),
#         ('science_mathematics', 'College of Science and Mathematics'),
#         ('science_tech_education', 'College of Science and Technology Education'),
#         ('technology', 'College of Technology'),
#         ('medicine', 'College of Medicine'),
#         ('senior_high_school', 'Senior High School'),
#     ]
    
#     # Constants for user roles
#     USER_ROLE_CHOICES = [
#         ('client', 'Client'),
#         ('employee', 'Employee'),
#         ('admin', 'Admin'),
#     ]

#     # Constants for school campuses
#     SCHOOL_CAMPUS_CHOICES = [
#         ('ustp_alubijid', 'USTP Alubijid'),
#         ('ustp_cagayan_de_oro', 'USTP Cagayan de Oro'),
#         ('ustp_claveria', 'USTP Claveria'),
#         ('ustp_balubal', 'USTP Balubal'),
#         ('ustp_jasaan', 'USTP Jasaan'),
#         ('ustp_oroquieta', 'USTP Oroquieta'),
#         ('ustp_panaon', 'USTP Panaon'),
#         ('ustp_villanueva', 'USTP Villanueva'),
#     ]

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_groups',
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

#     first_name = models.CharField(max_length=255)
#     middle_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=200, unique=True)
#     birth_date = models.DateField()
#     contact_number = models.CharField(max_length=12, blank=True)  # Allow blank
#     school_campus = models.CharField(max_length=50, choices=SCHOOL_CAMPUS_CHOICES, default='ustp_cagayan_de_oro')
#     department_type = models.CharField(max_length=50, choices=COLLEGE_CHOICES, default='information_technology')
#     user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='client')

#     def generate_default_password(self):
#         birthday_string = self.birth_date.strftime('%m%d%Y')
#         default_password = f"{self.last_name.lower()}@{birthday_string}"
#         return default_password

#     def save(self, *args, **kwargs):
#         if not self.pk:  # If this is a new instance
#             default_password = self.generate_default_password() 
#             self.password = make_password(default_password)
#         super().save(*args, **kwargs)

#     def is_admin(self):
#         return self.user_role == 'admin'

#     def is_employee(self):
#         return self.user_role == 'employee'

#     def is_client(self):
#         return self.user_role == 'client'

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
#     username=None

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     USERNAME_REQUIRED = False


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
    user_role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='client')