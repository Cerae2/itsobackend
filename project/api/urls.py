from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('feedback/', include('feedbackstatus.urls')),
    path('uploadforms/', include('formupload.urls')),
]