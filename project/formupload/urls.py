# uploadforms/urls.py
from django.urls import path
from .views import (
    UploadFormListCreateAPIView,
    UploadFormRetrieveUpdateDestroyAPIView,
    FeedbackListCreateAPIView,
    FeedbackRetrieveUpdateDestroyAPIView,
    FileUploadListCreateAPIView,
    FileUploadRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('forms/', UploadFormListCreateAPIView.as_view(), name='upload-forms-list'),
    path('forms/<int:pk>/', UploadFormRetrieveUpdateDestroyAPIView.as_view(), name='upload-forms-detail'),
    path('feedbacks/', FeedbackListCreateAPIView.as_view(), name='feedbacks-list'),
    path('feedbacks/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedbacks-detail'),
    path('file/', FileUploadListCreateAPIView.as_view(), name='file-uploads-list'),
    path('file/<int:pk>/', FileUploadRetrieveUpdateDestroyAPIView.as_view(), name='file-uploads-detail'),
]
