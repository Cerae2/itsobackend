from django.db import models

class UtilityFile(models.Model):

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='utilitymodelfiles/')
  
    def __str__(self):
        return self.title
