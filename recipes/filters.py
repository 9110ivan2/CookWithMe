from recipes.models import Recipe
import django_filters as filters
from django_filters.rest_framework import FilterSet

class RecipeFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(field_name='author__username', lookup_expr='icontains')


    class Meta:
        model = Recipe
        fields = ['title', 'author']