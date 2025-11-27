from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, PaketViewSet, TrackingViewSet

# Buat sebuah router dan daftarkan ViewSet kita
router = DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='api-customer')
router.register(r'paket', PaketViewSet, basename='api-paket')
router.register(r'tracking', TrackingViewSet, basename='api-tracking')

# URL API sekarang ditentukan secara otomatis oleh router.
urlpatterns = [
    path('', include(router.urls)),
]