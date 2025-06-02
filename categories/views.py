from rest_framework import generics, permissions
from categories.models import Category
from categories.serializers import Categoryserializer
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import  AllowAny

# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print("DEBUG: request.user =", request.user) # TODO remove in production
        print("DEBUG: is_authenticated =", request.user.is_authenticated) # TODO remove in production
        print("DEBUG: is_superuser =", request.user.is_superuser) # TODO remove in production
        if not request.user.is_authenticated or not request.user.is_superuser:
            return Response({"error": "You must be logged in to create a category."}, status=status.HTTP_403_FORBIDDEN)
        return self.create(request, *args, **kwargs)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = Categoryserializer
