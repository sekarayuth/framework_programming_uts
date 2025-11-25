from django import forms
from .models import Customer, Paket, Tracking

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['nik', 'nama', 'alamat', 'kota', 'no_telepon']
        widgets = {
            'nik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NIK / KTP'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap Pengirim'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Alamat Lengkap'}),
            'kota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kota Domisili'}),
            'no_telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08xxxxxx'}),
        }

class PaketForm(forms.ModelForm):
    class Meta:
        model = Paket
        # Resi DIHAPUS dari sini, biar user cuma isi data pengiriman
        fields = ['pengirim', 'penerima', 'alamat_tujuan', 'layanan', 'berat']
        widgets = {
            'pengirim': forms.Select(attrs={'class': 'form-select bg-light'}), # Kita buat agak abu karena otomatis
            'penerima': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Penerima Paket'}),
            'alamat_tujuan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Alamat Lengkap Tujuan'}),
            'layanan': forms.Select(attrs={'class': 'form-select'}),
            'berat': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Berat (Kg)'}),
        }

class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = ['paket', 'status', 'lokasi']
        widgets = {
            'paket': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'lokasi': forms.TextInput(attrs={'class': 'form-control'}),
        }