from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('file/', include('fileupload.urls')),
    # Other app-specific URLs...
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
