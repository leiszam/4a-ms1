from django.urls import path
from .views import UserGetData, UserListCreate,UserUpdateDelete,UserGetSerializer

urlpatterns = [
    path('usuario/', UserListCreate.as_view()),
    path('usuario/<pk>/', UserUpdateDelete.as_view()),
    path('user/', UserGetData.as_view()),
]