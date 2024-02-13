from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import User as CustomUser
from .serializers import CustomUserSerializer
from formupload.models import UploadForms

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




class UploadsByYearView(ListAPIView):
    serializer_class = None  # Assuming no serialization is needed for this example

    def list(self, request, *args, **kwargs):
        # Extract the year from the query parameters
        year = request.query_params.get('year')

        if not year:
            return Response({"error": "Year is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Convert the year to an integer to ensure it's valid
            year = int(year)
        except ValueError:
            return Response({"error": "Invalid year format"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter uploads based on the year
        uploads = UploadForms.objects.filter(uploaded_at__year=year)

        # If you need to serialize the data, you can do so here before returning the response
        # For example, using a custom serializer:
        # serializer = UploadFormSerializer(uploads, many=True)
        # return Response(serializer.data)

        # Return the list of uploads in the response
        return Response({'uploads': list(uploads.values())})
