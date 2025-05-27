from django.urls import path
from categories.views import RecipeListCreateView, RecipeDetailView, CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("recipe-list-create", RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("recipe-detail/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("category-list-create", CategoryListCreateView.as_view(), name="category-list-create"),
    path("category-detail/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]