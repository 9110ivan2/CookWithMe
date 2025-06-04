from django.shortcuts import render
from reviews.models import Review
from rest_framework import generics, permissions
from reviews.serializers import ReviewSerializer
from reviews.permissions import IsAuthorOrAdmin


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorOrAdmin]
