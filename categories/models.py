from django.db import models
from recipes.models import Recipe
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        related_name='subcategories', 
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name_plural= 'Categories' 

    
    def __str__(self):
        return self.name
