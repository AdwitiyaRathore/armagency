from django.db import models
from django.contrib import auth

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    # str reprasentation of username.
    def __str__(self):
        return self.username