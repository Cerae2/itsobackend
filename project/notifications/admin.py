from django.contrib import admin
from .models import Notification
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display=['id','sender','receiver','is_read']
admin.site.register(Notification,NotificationAdmin)
