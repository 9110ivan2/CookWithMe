from django.urls import path
from recipes.views import RecipeListCreateView, RecipeDetailView
from reviews.views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path("category-detail/recipes/",RecipeListCreateView.as_view(), name="recipe-list-create"),
    path("category-detail/<int:category_id>/recipes/", RecipeListCreateView.as_view(), name="by-id-recipe-list-create"),
    path("category-detail/<int:category_id>/recipes/<int:pk>/", RecipeListCreateView.as_view(), name="by-id-recipe-list-create"),
    path("category-detail/<int:category_id>/recipe-detail/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("category-detail/<int:category_id>/recipe-detail/<int:pk>/reviews/", ReviewListCreateView.as_view(), name="recipe-reviews"),
    path("category-detail/<int:category_id>/recipe-detail/<int:pk>/reviews/<int:review_pk>/", ReviewDetailView.as_view(), name="recipe-review-detail"),
    
    # /recipes/?title=chicken
    # /recipes/?author=JohnDoe
    # /recipes/?title=chicken&author=JohnDoe to filter recipes by title and author
]