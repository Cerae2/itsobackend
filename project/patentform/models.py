# another_file_upload_app/models.py
from django.db import models

class PatentUpload(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('rejected', 'Rejected'),
    ]

    invention_title = models.CharField(max_length=255, null=True)
    abstract = models.TextField(max_length=300, null=True)
    patent_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    Patent_file_1 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    Patent_file_2 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    Patent_file_3 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    Patent_file_4 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
