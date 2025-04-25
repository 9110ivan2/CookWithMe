from django.shortcuts import generics
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetailView(generics.RetrieveUpdateDestoryAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# Create your views here.
