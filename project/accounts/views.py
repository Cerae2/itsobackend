from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import User as CustomUser
from .serializers import CustomUserSerializer

class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'campus'

    def filter_queryset(self, queryset):
        return queryset.filter(school_campus = self.kwargs['campus'])


class CampusesListView(ListAPIView):
    queryset = CustomUser.objects.exclude(school_campus__isnull=True).values_list('school_campus', flat=True).distinct()
    serializer_class = None  # No serializer needed since we're returning raw data

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        campuses = list(queryset)
        return Response({'campuses': campuses})


class DepartmentsByCampusView(ListAPIView):
    serializer_class = None  # We won't use a serializer here, just returning raw data

    def list(self, request, *args, **kwargs):
        # Get the campus name from the query parameters
        campus_name = request.query_params.get('campus')

        if not campus_name:
            return Response({"error": "Campus name is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter departments based on the campus name
        departments = CustomUser.objects.filter(school_campus=campus_name).values_list('department_type', flat=True).distinct()

        # Return the list of departments in the response
        return Response({'departments': list(departments)})





