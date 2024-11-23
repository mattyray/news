from django.db import models
from django.contrib.auth.models import AbstractUser

# models.py in accounts or a new quizzes app



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)  # Optional bio field  # Optional profile picture

