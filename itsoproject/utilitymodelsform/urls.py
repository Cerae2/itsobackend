from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilityFileViewSet

router = DefaultRouter()
router.register(r'files', UtilityFileViewSet, basename='files')

urlpatterns = [
    path('', include(router.urls)),
]
