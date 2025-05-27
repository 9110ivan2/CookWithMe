from django.shortcuts import generics
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from recipes.filters import RecipeFilter
from django_filters.rest_framework import DjangoFilterBackend


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter


class RecipeDetailView(generics.RetrieveUpdateDestoryAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# Create your views here.
