from django.urls import path
from .views import UserListCreate,UserUpdateDelete

urlpatterns = [
    path('usuario/', UserListCreate.as_view()),
    path('usuario/<pk>/', UserUpdateDelete.as_view()),
]