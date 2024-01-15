from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('industrialforms/', include('industrialform.urls')),
    path('utilityforms/', include('utilityform.urls')),
    path('patentforms/', include('patentform.urls')),
    path('trademarkforms/', include('trademarkform.urls')),
    path('copyrightforms/', include('copyrightform.urls')),
    # Other app-specific URLs...
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
