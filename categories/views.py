from rest_framework import generics, permissions
from categories.models import Category, RecipeCategory
from categories.serializers import Categoryserializer, RecipeCategoryserializer
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

    def post(self, request, *args, **kwargs):
        if not request.superuser.is_authenticated:
            return Response({"error": "You must be logged in to create a category."}, status=status.HTTP_403_FORBIDDEN)
        return self.create(request, *args, **kwargs)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = Categoryserializer

class RecipeListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategoryserializer

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategoryserializer