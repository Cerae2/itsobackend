from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    UTILITY_MODEL = 'utility_model'
    INDUSTRIAL_DESIGN = 'industrial_design'
    TRADEMARK = 'trademark'
    PATENT = 'patent'
    COPYRIGHT = 'copyright'
    
    DOCUMENT_TYPES = [
        (UTILITY_MODEL, 'Utility Model'),
        (INDUSTRIAL_DESIGN, 'Industrial Design'),
        (TRADEMARK, 'Trademark'),
        (PATENT, 'Patent'),
        (COPYRIGHT, 'Copyright'),
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    feedback = models.TextField(blank=True, null=True)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES, null=True, default=UTILITY_MODEL)  # Allow null and provide a default value

    def __str__(self):
        return self.title
