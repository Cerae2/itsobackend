# another_file_upload_app/models.py
from django.db import models

class TrademarkUpload(models.Model):
    trademark_file_1 = models.FileField(upload_to='trademarkforms/', null=True, blank=True)
    trademark_file_2 = models.FileField(upload_to='trademarkforms/', null=True, blank=True)
    trademark_file_3 = models.FileField(upload_to='trademarkforms/', null=True, blank=True)
    trademark_file_4 = models.FileField(upload_to='trademarkforms/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
