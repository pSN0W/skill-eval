from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Custom user model 
    """
    name = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)