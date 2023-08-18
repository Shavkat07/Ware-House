from rest_framework.serializers import ModelSerializer

from .models import Provider, Income, IncomeItem


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class IncomeItemSerializer(ModelSerializer):
    class Meta:
        model = IncomeItem
        fields = '__all__'
