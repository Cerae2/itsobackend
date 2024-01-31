from django.contrib import admin
from .models import Feedback, FileUploads, UploadForms
# Register your models here.

admin.site.register(UploadForms)
admin.site.register(Feedback)
admin.site.register(FileUploads)