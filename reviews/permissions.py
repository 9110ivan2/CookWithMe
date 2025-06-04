from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        # Allow if user is admin
        if user.is_staff or user.is_superuser:
            return True
        # Allow if user is author of the review
        if hasattr(obj, 'author') and obj.author == user:
            return True
        return False
