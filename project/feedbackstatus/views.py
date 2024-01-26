from rest_framework import generics
from .models import FeedbackstatusAPI
from .serializers import FeedbackstatusSerializer

class FeedbackstatusCreateView(generics.ListCreateAPIView):
    queryset = FeedbackstatusAPI.objects.all()
    serializer_class = FeedbackstatusSerializer