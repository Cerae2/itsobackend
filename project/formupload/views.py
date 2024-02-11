from .models import UploadForms, Feedback, FileUploads
from .serializers import UploadFormSerializers, FeedbackSerializer, FileUploadsSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import status
from notification.models import Notification
from accounts.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

class UploadFormListCreateAPIView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UploadFormSerializers  

    def get_queryset(self):
        queryset = UploadForms.objects.none()

        if self.request.user.is_authenticated:
       
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
                    if self.request.user.is_authenticated:
                        user = self.request.user
                        queryset = UploadForms.objects.filter(user=user)  
        else:
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


        return queryset

class UploadFormRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UploadForms.objects.all()
    serializer_class = UploadFormSerializers 
       


class FeedbackListCreateAPIView(ListCreateAPIView):
    serializer_class = FeedbackSerializer    

    def get_queryset(self):   
        upload_form = self.request.GET.get('upload_form')
        print("upload id", upload_form)
        upload_form_id = UploadForms.objects.get(id=upload_form)
        queryset = Feedback.objects.filter(upload_form=upload_form_id)

        return queryset
    
    def create(self, request, *args, **kwargs):
        upload_form = request.data['upload_form']
        feedback_text = request.data['feedback_text']
        file_status = request.data['file_status']

        upload_form_id = UploadForms.objects.get(id=upload_form)

        new_feedback = Feedback.objects.create(
            upload_form=upload_form_id,
            feedback_text=feedback_text,
            file_status=file_status
        )
        new_feedback.save()

        if file_status == "Approved":
            new_notification = Notification.objects.create(
                owner=self.request.user,
                recipient=upload_form_id.user,
                subject="Your form has been approved.",
                upload_form=upload_form 
            )
            new_notification.save()
        elif file_status == "Under Review":
            new_notification = Notification.objects.create(
                owner=self.request.user,
                recipient=upload_form_id.user,
                subject="Your form is currently under review.",
                upload_form=upload_form 
            )
            new_notification.save()
        elif file_status == "Rejected":
            new_notification = Notification.objects.create(
                owner=self.request.user,
                recipient=upload_form_id.user,
                subject="Your form has been rejected.",
                upload_form=upload_form 
            )
            new_notification.save()

        existing_upload_form = UploadForms.objects.filter(id=upload_form)
        if existing_upload_form.exists():
            existing_upload_form.update(upload_status=file_status)

        return Response({"message:", "Success"})


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
        add_new_file = request.data.get('add_new_file')
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

        
        try:
            admins = User.objects.filter(user_role='admin')
            
            owner = User.objects.get(username=self.request.user) 
            if add_new_file is not None:
                add_new_file = add_new_file.lower() == 'true'

            if add_new_file:
                for admin in admins:
                    new_notification = Notification.objects.create(
                        owner=owner,
                        recipient=admin,
                        subject=f'{self.request.user} added a new file.',
                        upload_form=upload_form_id
                    )
                    new_notification.save()
            else:
                for admin in admins:
                    new_notification = Notification.objects.create(
                        owner=owner,
                        recipient=admin,
                        subject=f'{self.request.user} submitted a new form.',
                        upload_form=upload_form_id
                    )
                    new_notification.save()
        except ObjectDoesNotExist as e:
            
            print(f"Error creating notification: {e}")
            return Response({"detail": "Failed to create notification."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
      
            print(f"Unexpected error: {e}")
            return Response({"detail": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        return Response({"success": f"{len(files)} files uploaded successfully."}, status=status.HTTP_201_CREATED)
        

class FileUploadRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FileUploads.objects.all()
    serializer_class = FileUploadsSerializer

