from django.urls import path
from .views import UploadFormAPIView, CustomFileListView

app_name = 'upload_app'

urlpatterns = [
    path('', UploadFormAPIView.as_view(), name='upload_form'),
    path('filelist', CustomFileListView.as_view()),
    # Add other URLs for different functionalities if needed
]
