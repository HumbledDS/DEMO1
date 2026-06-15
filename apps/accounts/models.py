from symtable import Class
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

""" class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username """

class User(AbstractUser):
    # Ajoutez des champs personnalisés ici si 
    bio=models.CharField(max_length=200, blank=True, null=True)
    organisation=models.CharField(max_length=100, blank=True)

