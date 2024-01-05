# another_file_upload_app/models.py
from django.db import models

class UtilityUpload(models.Model):
    utility_file_1 = models.FileField(upload_to='utilityforms/', null=True, blank=True)
    utility_file_2 = models.FileField(upload_to='utilityforms/', null=True, blank=True)
    utility_file_3 = models.FileField(upload_to='utilityforms/', null=True, blank=True)
    utility_file_4 = models.FileField(upload_to='utilityforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
