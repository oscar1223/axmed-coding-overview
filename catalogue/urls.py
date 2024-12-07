# catalogue/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicationSKUViewSet

router = DefaultRouter()
router.register(r'skus', MedicationSKUViewSet, basename='sku')

urlpatterns = [
    path('', include(router.urls)),
]
