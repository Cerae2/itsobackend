# another_file_upload_app/models.py
from django.db import models

class CopyrightUpload(models.Model):
    copyright_file_1 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    copyright_file_2 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    copyright_file_3 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    copyright_file_4 = models.FileField(upload_to='copyrightforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
