from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Client, Order, OrderItem
from .serializers import ClientSerializer, OrderSerializer, OrderItemSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
