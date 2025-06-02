from django.urls import path
from categories.views import CategoryListCreateView, CategoryDetailView 
urlpatterns = [
    path("category-list-create/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("category-detail/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]