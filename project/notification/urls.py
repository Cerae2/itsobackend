from django.urls import path
from . import views

urlpatterns = [
    path('fetch/', views.NotificationListCreateView.as_view(), name='notification-list'),
    path('update-read-status/', views.NotificationUpdateView.as_view(), name='notification-list'),
]
