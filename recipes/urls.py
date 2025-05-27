from django.urls import path
from recipes.views import RecipeListCreateView, RecipeDetailView

urlpatterns = [
    path("recipes/", RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("recipe-detail/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    #/recipes/?title=chicken
    #/recipes/?author=JohnDoe
    #/recipes/?title=chicken&author=JohnDoe to filter recipes by title and author

]