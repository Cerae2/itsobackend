# messenger_chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:username>/', views.chat, name='chat'),
    path('send_message/<str:username>/', views.send_message, name='send_message'),
]
