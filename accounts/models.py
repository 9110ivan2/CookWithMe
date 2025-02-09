from django.db import models
from django.contrib.auth.models import AbstractUser, User 


class User_customer(AbstractUser):
    #TODO problem with the user class needs to be renamed due to User built-in naming 

    email = models.EmailField(unique=True) #TODO the email column is not unique in the db postgres has to be changed.

    REQUIRED_FIELDS = ["email"]
    groups = None
    user_permissions = None

    def __str__(self):
        return self.username


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
   # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) need to add Pillow model
    location = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"