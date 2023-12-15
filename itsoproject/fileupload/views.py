from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')
        document_type = request.data.get('document_type')

        if not uploaded_file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        allowed_formats = {
            'utility_model': '.pdf',
            'industrial_design': '.pdf',
            'trademark': '.pdf',
            'patent': '.pdf',
            'copyright': '.pdf'
        }

        if not uploaded_file.name.lower().endswith(allowed_formats.get(document_type, '')):
            return Response({'error': f'Invalid file format for {document_type}. Only PDF files are allowed.'}, status=status.HTTP_400_BAD_REQUEST)

        file_instance = UploadedFile(file=uploaded_file, uploaded_by=request.user, title=uploaded_file.name, document_type=document_type)
        file_instance.save()

        serializer = self.get_serializer(file_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
