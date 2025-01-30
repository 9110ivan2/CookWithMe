from django.db import models
from django.contrib.auth.models import AbstractUser, User 


class User(AbstractUser):

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email"]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True

    )

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