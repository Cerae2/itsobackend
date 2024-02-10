from django.db import models
from django.conf import settings
from accounts.models import User



class UploadForms(models.Model):
    

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    form_type = models.CharField(max_length=50, null=True, blank=True)
    invention_title = models.CharField(max_length=255, null=True)
    summary = models.TextField(max_length=300, null=True)
    authors = models.TextField(max_length=300, null=True)
    upload_status = models.CharField(max_length=50, null=True, blank=True, default='Pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


    def all_files_approved(self):
        return self.file_uploads.filter(feedbacks__file_status='approved').count() == self.file_uploads.count()
    
class Feedback(models.Model):
   
    upload_form = models.ForeignKey(UploadForms, on_delete=models.CASCADE, null=True, blank=True)
    file_status = models.CharField(max_length=20, null=True, blank=True)
    feedback_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}'

class Fileup(models.Model):
    files = models.ManyToManyField('FileUploads', related_name='upload_files', blank=True)
    # Other fields in your model

class FileUploads(models.Model):
    # Assuming you have a model named UploadForms, adjust as needed
    upload_form = models.ForeignKey(UploadForms, on_delete=models.CASCADE, related_name='file_uploads')
    file = models.FileField(upload_to='uploads/', blank=False, null=False)
    file_name = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.upload_form.all_files_approved():
            self.upload_form.upload_status = 'approved'
            self.upload_form.save()




