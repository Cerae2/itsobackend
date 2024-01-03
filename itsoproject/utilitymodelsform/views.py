from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UtilityFile
from .serializers import UtilityFileSerializers

class UtilityFileViewSet(viewsets.ModelViewSet):
    queryset = UtilityFile.objects.all()
    serializer_class = UtilityFileSerializers
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        allowed_formats = {
            'utility_model': '.pdf',
        }

        document_type = request.data.get('document_type')
        if document_type and not uploaded_file.name.lower().endswith(allowed_formats.get(document_type, '')):
            return Response({'error': f'Invalid file format for {document_type}. Only PDF files are allowed.'}, status=status.HTTP_400_BAD_REQUEST)

        file_instance = UtilityFile(file=uploaded_file, title=uploaded_file.name)
        file_instance.save()

        serializer = self.get_serializer(file_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

