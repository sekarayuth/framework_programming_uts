from rest_framework import serializers
from .models import Customer, Paket, Tracking

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'

class PaketSerializer(serializers.ModelSerializer):
    # Nested Serializer: Menampilkan history tracking di dalam data paket
    tracking_history = TrackingSerializer(many=True, read_only=True, source='tracking')
    class Meta:
        model = Paket
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    # Nested Serializer: Menampilkan daftar paket yang dikirim customer ini
    daftar_paket = PaketSerializer(many=True, read_only=True, source='paket_dikirim')
    class Meta:
        model = Customer
        fields = '__all__'