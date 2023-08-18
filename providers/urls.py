from rest_framework.routers import SimpleRouter
from .views import ProviderViewSet, IncomeViewSet, IncomeItemViewSet

router = SimpleRouter()

router.register("providers", ProviderViewSet)
router.register("income", IncomeViewSet)
router.register("incomeitem", IncomeItemViewSet)

urlpatterns = [

]
