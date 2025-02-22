from django.db import models
from django.conf import settings
from recipes.models import Recipe
from django.contrib.auth.models import User
# Create your models here.

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by') #TODO check again the related name if it is full 
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together= ('user','recipe')
        ordering= ['-added_at']


    def __str__(self):
        return f"{self.user.username} liked {self.recipe.title}"