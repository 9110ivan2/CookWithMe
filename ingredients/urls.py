from django.urls import path
from ingredients.views import IngredientListCreateView, IngredientDetailView, RecipeIngredientListCreateView, RecipeIngredientDetailView
urlpatterns = [
    path("ingredient-list-create", IngredientListCreateView.as_view(), name="ingredient-list-create"),
    path("ingredient-detail/<int:pk>/", IngredientDetailView.as_view(), name="ingredient-detail"),
    path("recipe-ingredient-list-create", RecipeIngredientListCreateView.as_view(), name="recipe-ingredient-list-create"),
    path("recipe-ingredient-detail/<int:pk>/", RecipeIngredientDetailView.as_view(), name="recipe-ingredient-detail"),
]