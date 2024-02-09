from .models import UploadForms, Feedback, FileUploads
from .serializers import UploadFormSerializers, FeedbackSerializer, FileUploadsSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status


class UploadFormListCreateAPIView(ListCreateAPIView):
 
    serializer_class = UploadFormSerializers  
    def get_queryset(self):
        queryset = UploadForms.objects.none()
        select_invention = self.request.GET.get('select_invention')
        is_admin = self.request.GET.get('is_admin')
        

        print('is_admin', is_admin)

        if select_invention is not None:
            select_invention = select_invention.lower() == 'true'
        
        if is_admin is not None:
            is_admin = is_admin.lower() == 'true'
        
        if is_admin:
            
            print('select_invention', select_invention)
            print('admin ni')
            if select_invention:
                id = self.request.GET.get('id')
                queryset = UploadForms.objects.filter(id=id)
                print('select')
            else:
                queryset = UploadForms.objects.all()
                print('not select')
                
        else:
            print('select_invention', select_invention)
            print('client ni')
            if select_invention:
                id = self.request.GET.get('id')
                queryset = UploadForms.objects.filter(id=id)
            else:
                user = self.request.user
                queryset = UploadForms.objects.filter(user=user)  


        return queryset

class UploadFormRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers    


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer    

class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer    

class FileUploadListCreateAPIView(ListCreateAPIView):
    queryset = FileUploads.objects.all()
    serializer_class = FileUploadsSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    def create(self, request, *args, **kwargs):
        print("Received FILES:", request.FILES)
        upload_form_id = request.data.get('upload_form')
        if not upload_form_id:
            return Response({"detail": "No upload_form ID was submitted."}, status=status.HTTP_400_BAD_REQUEST)

        upload_form_obj = UploadForms.objects.get(id=upload_form_id)
        files = request.FILES.getlist('files')

        if not files:
            return Response({"detail": "No files were submitted."}, status=status.HTTP_400_BAD_REQUEST)

        for file in files:
            new_file = FileUploads.objects.create(
                file_name=file.name,
                file=file,
                upload_form=upload_form_obj
            )
            new_file.save()

        return Response({"success": f"{len(files)} files uploaded successfully."}, status=status.HTTP_201_CREATED)
        

class FileUploadRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FileUploads.objects.all()
    serializer_class = FileUploadsSerializer

