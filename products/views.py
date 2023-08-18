from .serializers import ProductsSerializers, CategorySerializers
from .models import Products, Category
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
