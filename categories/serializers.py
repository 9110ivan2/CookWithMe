from rest_framework import serializers
from categories.models import Category, RecipeCategory

class Categoryserializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields ="__all__"


class RecipeCategoryserializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeCategory
        fields = "__all__"