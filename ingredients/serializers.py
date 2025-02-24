from rest_framework import serializer
from ingredients.models import Ingredient, RecipeIngredient


class IgredientSerializer(serializer.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeIngredientSerializer(serializer.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"
