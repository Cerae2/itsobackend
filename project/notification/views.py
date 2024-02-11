from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics

class NotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        
        user = self.request.user  
        return Notification.objects.filter(recipient=user)
    

class NotificationUpdateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user  
        Notification.objects.filter(recipient=user).update(read_status=True)
        return Notification.objects.filter(recipient=user)
