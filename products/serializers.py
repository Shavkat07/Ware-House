from rest_framework.serializers import ModelSerializer
from .models import Category, Products


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

