# uploadforms/urls.py
from django.urls import path
from .views import NotificationListCreateAPIView, NotificationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('notifications/', NotificationListCreateAPIView.as_view(), name='notifications_list_create'),
    path('notifications/<pk>/', NotificationRetrieveUpdateDestroyAPIView.as_view(), name='notifications_list_create'),

]
