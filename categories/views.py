from rest_framework import generics
from categories.models import Category, RecipeCategory
from categories.serializers import Categoryserializer, RecipeCategoryserializer

# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategoryserializer

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategoryserializer