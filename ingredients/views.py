from rest_framework import generics
from ingredients.models import Ingredient, RecipeIngredient
from ingredients.serializers import IgredientSerializer, RecipeIngredientSerializer

class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IgredientSerializer

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IgredientSerializer

class RecipeIngredientListCreateView(generics.ListCreateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

class RecipeIngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer

# Create your views here.
