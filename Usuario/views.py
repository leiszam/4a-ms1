from django.shortcuts import render
from rest_framework import views, generics,authentication,permissions, status
from rest_framework.serializers import Serializer
from .models import CustomUser 
from .serializers import UsuarioSerielizer , UserGetSerializer

from rest_framework.response import Response

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerielizer
    #authentication_classe = [authentication.TokenAuthentication]
    #permissions_classes = [permissions.IsAuthenticated]

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerielizer

class UserGetData(views.APIView):
    authentication_classe = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
    
        serializer = UserGetSerializer(request.user)
        return Response(data=serializer.data, status = status.HTTP_200_OK)
        
