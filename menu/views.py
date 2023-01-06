from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from .models import Menu
from .serializers import MenuSerializer


class MenuView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    lookup_url_kwarg = "pk"
