from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomUserListView
from .views import DepartmentsByCampusView
from .views import CampusesListView

# urlpatterns = [
#     path('login/', obtain_auth_token, name='api_token_auth'),  # Login endpoint
#     path('register/', CustomUserCreateView.as_view(), name='register'),  # Register endpoint
# ]


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('userlist/<str:campus>/', CustomUserListView.as_view()),
    path('departments/by_campus/', DepartmentsByCampusView.as_view(), name='departments_by_campus'),
    path('campuses/', CampusesListView.as_view(), name='campuses_list'),
]