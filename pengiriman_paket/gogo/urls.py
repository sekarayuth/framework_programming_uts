from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView, 
    CustomerUpdateView, CustomerDeleteView,
    
    PaketListView, PaketDetailView, PaketCreateView, 
    PaketUpdateView, PaketDeleteView,

    TrackingCreateView
)

urlpatterns = [
    # --- URL CUSTOMER ---
    # Perhatikan bagian name='...' sudah disamakan dengan template HTML
    path('', CustomerListView.as_view(), name='customer-list'),
    path('tambah/', CustomerCreateView.as_view(), name='customer-add'), # Sebelumnya customer-tambah
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer-edit'),
    path('<int:pk>/hapus/', CustomerDeleteView.as_view(), name='customer-delete'), # Sebelumnya customer-hapus

    # --- URL PAKET ---
    path('paket/', PaketListView.as_view(), name='paket-list'),
    path('paket/tambah/', PaketCreateView.as_view(), name='paket-add'), # Sebelumnya paket-tambah
    path('paket/<int:pk>/', PaketDetailView.as_view(), name='paket-detail'),
    path('paket/<int:pk>/edit/', PaketUpdateView.as_view(), name='paket-edit'),
    path('paket/<int:pk>/hapus/', PaketDeleteView.as_view(), name='paket-delete'), # Sebelumnya paket-hapus

    # --- URL TRACKING ---
    path('tracking/tambah/', TrackingCreateView.as_view(), name='tracking-add'), # Sebelumnya tracking-tambah
]