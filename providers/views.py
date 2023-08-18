from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Provider, Income, IncomeItem
from .serializers import ProviderSerializer, IncomeSerializer, IncomeItemSerializer


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class IncomeViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = IncomeSerializer


class IncomeItemViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = IncomeItemSerializer

