from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
   # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) need to add Pillow model
    location = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"