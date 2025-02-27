from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, CarViewSet


router = DefaultRouter()

router.register(r'brands', BrandViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
