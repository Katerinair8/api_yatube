from django.core.exceptions import PermissionDenied

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.author != request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')

        return obj.author == request.user
