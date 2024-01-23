# another_file_upload_app/models.py
from django.db import models
from django.conf import settings


class UploadForms(models.Model):
    FORM_CHOICES = [
        ('patent_upload', 'Patent'),
        ('utility_model', 'Utility Model'),
        ('industrial_design', 'Industrial Design'),
        ('trade_mark', 'Trademark'),
        ('copy_right', 'Copyright'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    form_type = models.CharField(max_length=50, choices=FORM_CHOICES, default='patent_upload')
    invention_title = models.CharField(max_length=255, null=True)
    summary = models.TextField(max_length=300, null=True)
    authors = models.TextField(max_length=300, null=True)
    
    copyright_file_1 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    copyright_file_2 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    copyright_file_3 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    copyright_file_4 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
