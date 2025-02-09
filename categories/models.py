from django.db import models
from recipes.models import Recipe
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural= 'Categories' #TODO check what is this for 

    
    def __str__(self):
        return self.name
    

class RecipeCategory(models.Model):
    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_category')
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category') #TODO check exatly how is the related name writen 

    class Meta:
        unique_together=('recipe','category')

    def __str__(self):
        return f"{self.recipe.title} in {self.category.name}"