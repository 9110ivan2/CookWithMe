from rest_framework import generics
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from recipes.filters import RecipeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryRecipeQuerysetMixin:
    """
    Mixin to filter recipes by category_id if present in URL kwargs or query params.
    """
    def get_queryset(self):
        # Try to get category_id from URL kwargs first, then from query params
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Recipe.objects.filter(categories__id=category_id)
        return Recipe.objects.all()

    def perform_create(self, serializer):
        category_id = self.kwargs.get('category_id') or self.request.data.get('category_id')
        recipe = serializer.save(author=self.request.user)
        if category_id:
            recipe.categories.add(category_id)

class RecipeListCreateView(CategoryRecipeQuerysetMixin, generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter

class RecipeDetailView(CategoryRecipeQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer

    def delete(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        self.category_id = category_id
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category_id')
        self.category_id = category_id
        return super().put(request, *args, **kwargs)
