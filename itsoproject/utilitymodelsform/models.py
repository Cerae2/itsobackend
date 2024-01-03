from django.core.exceptions import ValidationError
from django.db import models

def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('File must be PDF.')

class UtilityFile(models.Model):
    title = models.CharField(max_length=255)
    file1 = models.FileField(upload_to='industrialdesignfiles/', blank=True, null=True, validators=[validate_pdf])
    file2 = models.FileField(upload_to='industrialdesignfiles/', blank=True, null=True, validators=[validate_pdf])
    file3 = models.FileField(upload_to='industrialdesignfiles/', blank=True, null=True, validators=[validate_pdf])
    file4 = models.FileField(upload_to='industrialdesignfiles/', blank=True, null=True, validators=[validate_pdf])
    
    def clean(self):
        # Ensure at least one file (file1 to file4) is provided
        if not (self.file1 or self.file2 or self.file3 or self.file4):
            raise ValidationError('At least one file (file1 to file4) is required.')

    def __str__(self):
        return self.title
