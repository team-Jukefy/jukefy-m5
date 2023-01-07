import ipdb
from django.utils.crypto import get_random_string
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User

from .models import Table
from .serializers import TableSerializer


class TableView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    user = User.objects.create(
        username=get_random_string(8),
        email=get_random_string(8),
        password=get_random_string(8),
    )

    def perform_create(self, serializer):
        serializer.save(user=self.user)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        token = AccessToken.for_user(self.user)
        token["table_id"] = self.user.table.id

        return Response({"token": str(token)})


class TableDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = TableSerializer
    queryset = Table.objects.all()

    lookup_url_kwarg = "pk"
