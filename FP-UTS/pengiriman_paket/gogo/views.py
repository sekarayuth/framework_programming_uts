from django.urls import reverse_lazy
from django.shortcuts import redirect
# Views Web
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Views API
from rest_framework import viewsets 
from .models import Customer, Paket, Tracking
from .forms import CustomerForm, PaketForm, TrackingForm
from .serializers import CustomerSerializer, PaketSerializer, TrackingSerializer

# === BAGIAN WEB (HTML) ===

class CustomerListView(ListView):
    model = Customer
    template_name = 'gogo/customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'gogo/customer_detail.html'

# 1. LOGIC MENAMBAH MEMBER
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'gogo/form.html'
    
    # ALUR KHUSUS: Setelah simpan member, JANGAN balik ke list.
    # TAPI lempar ke form paket sambil membawa ID member tersebut.
    def get_success_url(self):
        return reverse_lazy('paket-add') + f'?pengirim_baru={self.object.pk}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul_halaman'] = "Registrasi Member Pengirim"
        return context

# 2. LOGIC MENGIRIM PAKET
class PaketCreateView(CreateView):
    model = Paket
    form_class = PaketForm
    template_name = 'gogo/form.html'
    success_url = reverse_lazy('paket-list') # Selesai kirim paket, baru lihat daftar resi

    # OTOMATIS PILIH PENGIRIM
    def get_initial(self):
        initial = super().get_initial()
        # Cek apakah ada ID pengirim dari halaman sebelumnya?
        pengirim_id = self.request.GET.get('pengirim_baru')
        if pengirim_id:
            initial['pengirim'] = pengirim_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['judul_halaman'] = "Input Detail Pengiriman"
        return context

class PaketListView(ListView):
    model = Paket
    template_name = 'gogo/paket_list.html'

    # FITUR CARI RESI
    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('cari_resi')
        if keyword:
            queryset = queryset.filter(resi__icontains=keyword)
        return queryset

class PaketDetailView(DetailView):
    model = Paket
    template_name = 'gogo/paket_detail.html'

# ... (Sisa View Update/Delete dan Tracking sama seperti sebelumnya) ...
# Biar aman, copy saja class Update/Delete/Tracking dari kode sebelumnya jika mau lengkap
# Tapi inti permintaanmu ada di CustomerCreateView & PaketCreateView di atas.

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'gogo/form.html'
    success_url = reverse_lazy('customer-list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'gogo/confirm_delete.html'
    success_url = reverse_lazy('customer-list')

class PaketUpdateView(UpdateView):
    model = Paket
    form_class = PaketForm
    template_name = 'gogo/form.html'
    success_url = reverse_lazy('paket-list')

class PaketDeleteView(DeleteView):
    model = Paket
    template_name = 'gogo/confirm_delete.html'
    success_url = reverse_lazy('paket-list')

class TrackingCreateView(CreateView):
    model = Tracking
    form_class = TrackingForm
    template_name = 'gogo/form.html'
    success_url = reverse_lazy('paket-list')

# === BAGIAN API (Tetap ada tapi tidak muncul di web) ===
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class PaketViewSet(viewsets.ModelViewSet):
    queryset = Paket.objects.all()
    serializer_class = PaketSerializer

class TrackingViewSet(viewsets.ModelViewSet):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer