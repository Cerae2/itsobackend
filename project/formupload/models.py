from django.db import models
from django.conf import settings
from accounts.models import User

class UploadForms(models.Model):
    FORM_CHOICES = [
        ('patent_upload', 'Patent'),
        ('utility_model', 'Utility Model'),
        ('industrial_design', 'Industrial Design'),
        ('trade_mark', 'Trademark'),
        ('copy_right', 'Copyright'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('under_review', 'Under Review'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    form_type = models.CharField(max_length=50, choices=FORM_CHOICES, default='patent_upload')
    invention_title = models.CharField(max_length=255, null=True)
    summary = models.TextField(max_length=300, null=True)
    authors = models.TextField(max_length=300, null=True)
    upload_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


    def all_files_approved(self):
        return self.file_uploads.filter(feedbacks__file_status='approved').count() == self.file_uploads.count()

class Fileup(models.Model):
    files = models.ManyToManyField('FileUploads', related_name='upload_files', blank=True)
    # Other fields in your model

class FileUploads(models.Model):
    # Assuming you have a model named UploadForms, adjust as needed
    upload_form = models.ForeignKey(UploadForms, on_delete=models.CASCADE, related_name='file_uploads')
    file = models.FileField(upload_to='uploads/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.upload_form.all_files_approved():
            self.upload_form.upload_status = 'approved'
            self.upload_form.save()


class Feedback(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('under_review', 'Under Review'),
        ('rejected', 'Rejected'),
    ]

    file_upload = models.ForeignKey(FileUploads, on_delete=models.CASCADE, related_name='feedbacks')
    file_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    feedback_text = models.TextField()

    def __str__(self):
        return f'{self.id}'

