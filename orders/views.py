from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Order
from .serializers import OrderSerializer


class OrderView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DetailOrderView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
