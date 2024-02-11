from django.db import models
from accounts.models import User

class Notification(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='owner')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='recipient')
    upload_form = models.CharField(max_length=1000, null=True, blank=True)
    subject = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject