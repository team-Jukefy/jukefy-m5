from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import status, APIView, Request, Response
from users.models import User

from .models import Table
from .serializers import TableSerializer
from orders.serializers import OrderSerializer
from orders.models import Order
import ipdb


class TableView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get_anon_user(self):
        self.user = User.objects.create(
            username=get_random_string(8),
            email=get_random_string(8),
            password=get_random_string(8),
        )

        return self.user

    def perform_create(self, serializer):
        serializer.save(user=self.get_anon_user())

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


class TableOrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_url_kwarg = "pk"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(table_id=self.kwargs["pk"])

    def filter_queryset(self, queryset):
        return Order.objects.filter(table_id=self.kwargs["pk"])


class TableCloseView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def patch(self, request: Request, pk: int) -> Response:
        table = get_object_or_404(Table, id=pk)
        table.status = "available"
        table.save()
        User.objects.get(id=table.user.id).delete()
        Order.objects.filter(table_id=pk).update(payment="paid")

        return Response(status=status.HTTP_204_NO_CONTENT)
