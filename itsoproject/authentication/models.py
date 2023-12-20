from django.db import models
from django.contrib.auth.models import User

class Adduser(models.Model):
    # Department constants for different colleges and schools
    COLLEGE_OF_ENGINEERING_AND_ARCHITECTURE = 'college_of_engineering_and_architecture'
    COLLEGE_OF_INFORMATION_TECHNOLOGY_AND_COMPUTING = 'college_of_information_technology_and_computing'
    COLLEGE_OF_SCIENCE_AND_MATHEMATICS = 'college_of_science_and_mathematics'
    COLLEGE_OF_SCIENCE_AND_TECHNOLOGY_EDUCATION = 'college_of_science_and_technology_education'
    COLLEGE_OF_TECHNOLOGY = 'college_of_technology'
    COLLEGE_OF_MEDICINE = 'college_of_medicine'
    SENIOR_HIGH_SCHOOL = 'senior_high_school'
    
    # User role constants
    CLIENT = 'client'
    EMPLOYEE = 'employee'
    ADMIN = 'admin'
    
    # Choices for department types
    DEPARTMENT_TYPES = [
        (COLLEGE_OF_ENGINEERING_AND_ARCHITECTURE, 'College of Engineering and Architecture'),
        (COLLEGE_OF_INFORMATION_TECHNOLOGY_AND_COMPUTING, 'College of Information Technology and Computing'),
        (COLLEGE_OF_SCIENCE_AND_MATHEMATICS, 'College of Science and Mathematics'),
        (COLLEGE_OF_SCIENCE_AND_TECHNOLOGY_EDUCATION, 'College of Science and Technology Education'),
        (COLLEGE_OF_TECHNOLOGY, 'College of Technology'),
        (COLLEGE_OF_MEDICINE, 'College of Medicine'),
        (SENIOR_HIGH_SCHOOL, 'Senior High School'),
    ]
    
    # Choices for user roles
    USER_ROLE = [
        (CLIENT, 'Client'),
        (EMPLOYEE, 'Employee'),
        (ADMIN, 'Admin'),
    ]

    # User information fields
    name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    birth_date = models.DateField()
    campus = models.CharField(max_length=200)
    department_type = models.CharField(max_length=50, choices=DEPARTMENT_TYPES, null=True, default=None)
    user_role = models.CharField(max_length=20, choices=USER_ROLE, null=True, default=CLIENT)

    def __str__(self):
        return f"{self.name} {self.last_name}"  # Improved representation for the object
