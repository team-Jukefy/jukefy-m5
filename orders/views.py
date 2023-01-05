from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class OrderView(generics.ListAPIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DetailOrderView(generics.DestroyAPIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
