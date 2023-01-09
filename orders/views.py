from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, status

from .models import Order
from .serializers import OrderSerializer


class OrderView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderDetailView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
