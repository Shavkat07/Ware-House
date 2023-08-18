"""
URL configuration for Store_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .routers import DefaultRouter
from products.urls import router as products_router
from client.urls import router as client_router
from providers.urls import router as providers_router

router = DefaultRouter()
router.extend(products_router)
router.extend(client_router)
router.extend(providers_router)

schema_view = get_schema_view(
    openapi.Info(
        title="Mega Market API",
        default_version='v1',
        description="Mega Market Documentation using Front-End Developer",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shavkatkurbanov065@gmail.com"),
        license=openapi.License(name="MRIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path('swagger<json>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
