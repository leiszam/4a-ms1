from django.shortcuts import render
from rest_framework import generics,authentication,permissions
from .models import CustomUser
from .serializers import UsuarioSerielizer

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerielizer
    #authentication_classe = [authentication.TokenAuthentication]
    #permissions_classes = [permissions.IsAuthenticated]

class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UsuarioSerielizer