# models.py in the users Django app
from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    phone_number = models.CharField(max_length=30)
    first_name = models.CharField( max_length=40, verbose_name='first name')
    last_name = models.CharField(max_length=40, verbose_name='last name')
