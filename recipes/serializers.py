from rest_framework import serializer
from recipes.models import Recipe

class RecipeSerializer(serializer.ModelSerialzer):
    class Meta:
        model = Recipe
        fields = "__all__"