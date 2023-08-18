from rest_framework.routers import SimpleRouter
from .views import ClientViewSet, OrderViewSet, OrderItemViewSet

router = SimpleRouter()
router.register("clients", ClientViewSet)
router.register("order", OrderViewSet)
router.register("orderitem", OrderItemViewSet)

urlpatterns = [

]
