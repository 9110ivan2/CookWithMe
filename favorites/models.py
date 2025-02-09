from django.db import models
from django.conf import settings
from recipes.models import Recipe
from accounts.models import User_customer
# Create your models here.

class Favorites(models.Model):
    user = models.ForeignKey(User_customer, on_delete=models.CASCADE, related_name='user')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by') #TODO check again the related name if it is full 
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together= ('user','recipe')
        ordering= ['-added_at']


    def __str__(self):
        return f"{self.user.username} liked {self.recipe.title}"