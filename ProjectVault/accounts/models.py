from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomeUser(AbstractUser):
    # add your custome fields 
    email = models.EmailField(unique=True)
    profil_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    # Use email for login instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Django still requires this for createsuperuser

    def __str__(self):
        return self.email

