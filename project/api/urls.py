from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('uploadforms/', include('formupload.urls')),
    path('notifications/', include('notification.urls')),
    path('messenger_chat/', include('messenger_chat.urls')),
]