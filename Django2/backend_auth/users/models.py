# users/models.py
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')

    # Set the custom user manager
    objects = CustomUserManager()

    def __str__(self):
        return self.username
