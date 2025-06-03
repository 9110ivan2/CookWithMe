from django.urls import path
from recipes.views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path("category-detail/recipes/",RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("category-detail/<int:category_id>/recipes/", RecipeListCreateView.as_view(), name="by-id-recipe-list-create"),
    path("category-detail/<int:category_id>/recipe-detail/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    # /recipes/?title=chicken
    # /recipes/?author=JohnDoe
    # /recipes/?title=chicken&author=JohnDoe to filter recipes by title and author
]