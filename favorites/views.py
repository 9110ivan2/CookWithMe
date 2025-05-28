from rest_framework import generics
from favorites.models import Favorites
from favorites.serializers import FavoritesSerializer

# Create your views here.

class FavoritesListCreateView(generics.ListCreateAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer