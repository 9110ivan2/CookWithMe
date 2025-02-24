from rest_framework import serializer
from favorites.models import Favorites

class FavoritesSerializer(serializer.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"

        