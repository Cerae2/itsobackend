# another_file_upload_app/models.py
from django.db import models

class PatentUpload(models.Model):
    Patent_file_1 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    Patent_file_2 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    Patent_file_3 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    Patent_file_4 = models.FileField(upload_to='patentforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
