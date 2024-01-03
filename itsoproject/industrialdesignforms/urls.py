from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndustrialFileViewSet

router = DefaultRouter()
router.register(r'files', IndustrialFileViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
]
