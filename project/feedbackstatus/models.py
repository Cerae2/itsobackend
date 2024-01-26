from django.contrib.auth.models import AbstractUser
from django.db import models

class FeedbackstatusAPI(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('under_review', 'Under Review'),
        ('rejected','Rejected'),
    ]

    leave_feedback = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self) -> str:
        return f"feedback - {self.status}"