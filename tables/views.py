import ipdb
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from orders.models import Order
from orders.serializers import OrderSerializer
from users.models import User
from users.permissions import isOwnerOrAdmin

from .models import Table
from .permissions import TableExists
from .serializers import MusicSerializer, TableCloseSerializer, TableSerializer


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
    permission_classes = [IsAuthenticated]

    serializer_class = TableSerializer
    queryset = Table.objects.all()

    lookup_url_kwarg = "pk"


class MusicView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = MusicSerializer
    queryset = Table.objects.all()


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

    def get_paginated_response(self, data):
        assert self.paginator is not None

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        total_price = sum(
            [order["total_item_price"] for order in serializer.data],
        )

        return Response(
            {
                "count": self.paginator.page.paginator.count,
                "next": self.paginator.get_next_link(),
                "previous": self.paginator.get_previous_link(),
                "total_price": total_price,
                "results": data,
            }
        )


class TableCloseView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = TableCloseSerializer
    queryset = Table.objects.all()
