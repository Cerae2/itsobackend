from .models import UploadForms, Feedback, FileUploads
from .serializers import UploadFormSerializers, FeedbackSerializer, FileUploadsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UploadFormListCreateAPIView(ListCreateAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers    

class UploadFormRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers    


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer    

class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer    

class FileUploadListCreateAPIView(ListCreateAPIView):
    queryset = FileUploads.objects.all()
    serializer_class = FileUploadsSerializer    

class FileUploadRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FileUploads.objects.all()
    serializer_class = FileUploadsSerializer

