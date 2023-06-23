from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
# Create your models here.


class User(User, PermissionsMixin):
    def __str__(self):
        return self.username


class Doctor(User, PermissionsMixin):
    Phone_number = models.CharField(max_length=20)
    graduate_year = models.CharField(max_length=10)
    dental_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
