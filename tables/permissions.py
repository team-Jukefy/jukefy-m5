from rest_framework.permissions import BasePermission
from rest_framework.views import Request


class TableExists(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        if request.method == "POST":
            return not True in [
                True if table.status == "occupied" else False for table in obj
            ]
        return True


class OrderDetailPermission(BasePermission):
    def has_permission(self, request: Request, view):
        if hasattr(request.user, "table"):
            return request.user.table.id == view.kwargs["table_id"]

        return request.user.is_staff or request.user.is_superuser
