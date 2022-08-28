from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']

class UserProfile(models.Model):
    user = models.OneToOneField(
    # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"user: {self.user.username}; token: {self.token}"
