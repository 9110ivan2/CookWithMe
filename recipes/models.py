from django.db import models
from django.conf import settings
from django.utils.text import slugify
from accounts.models import Profile
from django.contrib.auth.models import User



# Create your models here.

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes') 
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    prep_time = models.PositiveIntegerField(help_text='Preparation time in minutes')
    cook_time= models.PositiveIntegerField(help_text='Cooking time in minutes')
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    categories = models.ManyToManyField(
        'categories.Category', 
        related_name='recipes', 
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

## class RecipeImage to be added. 