# catalogue/serializers.py

from rest_framework import serializers
from .models import MedicationSKU

class MedicationSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSKU
        fields = '__all__'

    def validate(self, data):
        # Validar la unicidad de la combinación
        if self.instance:
            # Para actualizaciones
            if MedicationSKU.objects.exclude(id=self.instance.id).filter(
                presentation=data['presentation'],
                dose=data['dose'],
                unit=data['unit']
            ).exists():
                raise serializers.ValidationError("La combinación de presentación, dosis y unidad ya existe.")
        else:
            # Para creaciones
            if MedicationSKU.objects.filter(
                presentation=data['presentation'],
                dose=data['dose'],
                unit=data['unit']
            ).exists():
                raise serializers.ValidationError("La combinación de presentación, dosis y unidad ya existe.")
        return data
