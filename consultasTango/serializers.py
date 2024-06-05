from rest_framework import serializers
from consultasTango.models import EB_facturaManual

class facturaManual(serializers.ModelSerializer):
    class Meta:
        model = EB_facturaManual
        fields = '__all__'