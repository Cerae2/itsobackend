from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('uploadforms/', include('uploadforms.urls')),
    path('feedback/', include('feedbackstatus.urls')),
]