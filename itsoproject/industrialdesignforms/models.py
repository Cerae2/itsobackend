from django.db import models

class IndustrialFile(models.Model):

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='industrialdesignfiles/')
  
    def __str__(self):
        return self.title
