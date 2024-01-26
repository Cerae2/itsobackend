from django.urls import path
from .views import FeedbackstatusCreateView

app_name = 'feedback_status'

urlpatterns = [
    path('', FeedbackstatusCreateView.as_view(), name='feedbackview'),
    # Add other URLs for different functionalities if needed
]
