from django.contrib.auth.hashers import make_password
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import Request
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .permissions import isOwnerOrAdmin
from .serializers import UserSerializer


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserDetailsView(RetrieveDestroyAPIView, UpdateModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, isOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request: Request, *args, **kwargs):
        if request.data.get("password"):
            request.data["password"] = make_password(request.data.get("password"))

        return self.partial_update(request, *args, **kwargs)
