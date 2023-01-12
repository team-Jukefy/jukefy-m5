from rest_framework.permissions import BasePermission
from rest_framework.views import Request

class TableExists(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        if request.method == "POST":
            return not True in [True if table.status == "occupied" else False for table in obj]
        return True
