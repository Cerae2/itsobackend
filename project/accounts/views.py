# from rest_framework.generics import CreateAPIView
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework import status
# from .models import CustomUser
# from .serializers import CustomUserSerializer

# class CustomUserCreateView(CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 token, _ = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
