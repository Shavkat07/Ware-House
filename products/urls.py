from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import CategoryViewSet, ProductsViewSet

app_name = 'products'

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("products", ProductsViewSet)

urlpatterns = [

]
