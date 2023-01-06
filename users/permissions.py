from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly


class isOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            (obj == request.user and request.method != "GET") or request.user.is_superuser
        )
