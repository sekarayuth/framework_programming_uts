import random
import string
from django.db import models

class Customer(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    kota = models.CharField(max_length=100)
    no_telepon = models.CharField(max_length=100)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

class Paket(models.Model):
    JENIS_LAYANAN = [
        ('REG', 'Reguler (2-3 Hari)'),
        ('EXP', 'Express (1 Hari)'),
        ('CARGO', 'Kargo (Min 10kg)'),
    ]
    
    resi = models.CharField(max_length=20, unique=True, blank=True)
    pengirim = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='paket_dikirim')
    penerima = models.CharField(max_length=100)
    alamat_tujuan = models.TextField()
    layanan = models.CharField(max_length=10, choices=JENIS_LAYANAN, default='REG')
    berat = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_kirim = models.DateTimeField(auto_now_add=True)

    #untuk resi otomatis
    def save(self, *args, **kwargs):
        if not self.resi:
            while True:
                angka = ''.join(random.choices(string.digits, k=8))
                calon_resi = f"GOGO-{angka}"
                if not Paket.objects.filter(resi=calon_resi).exists():
                    self.resi = calon_resi
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return self.resi

class Tracking(models.Model):
    STATUS = [
        ('DITERIMA', 'Paket Masuk ke Counter'),
        ('DIKIRIM', 'Sedang dalam Perjalanan'),
        ('SAMPAI', 'Paket Telah Diterima'),
    ]
    paket = models.ForeignKey(Paket, on_delete=models.CASCADE, related_name='tracking')
    status = models.CharField(max_length=30, choices=STATUS, default='DITERIMA')
    lokasi = models.CharField(max_length=100)
    waktu = models.DateTimeField(auto_now_add=True)