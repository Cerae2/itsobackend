# file_upload_app/models.py
from django.db import models

class IndustrialUpload(models.Model):
    industrial_file_1 = models.FileField(upload_to='industrialforms/', null=True, blank=True)
    industrial_file_2 = models.FileField(upload_to='industrialforms/', null=True, blank=True)
    industrial_file_3 = models.FileField(upload_to='industrialforms/', null=True, blank=True)
    industrial_file_4 = models.FileField(upload_to='industrialforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
