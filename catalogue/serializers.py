# catalogue/serializers.py

from rest_framework import serializers
from .models import MedicationSKU
from fuzzywuzzy import fuzz

class MedicationSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSKU
        fields = '__all__'

    def validate_medication_name(self, value):
        # Fuzzy matching para verificar unicidad aproximada
        existing_names = MedicationSKU.objects.values_list('medication_name', flat=True)
        for name in existing_names:
            similarity = fuzz.ratio(name.lower(), value.lower())
            if similarity > 90:
                raise serializers.ValidationError(
                    f"El nombre del medicamento '{value}' es similar a '{name}'. Por favor, verifica la unicidad."
                )
        return value

    def validate(self, data):
        # Validar la unicidad de la combinación (medication_name, presentation, dose, unit)
        if self.instance:
            # Para actualizaciones
            if MedicationSKU.objects.exclude(id=self.instance.id).filter(
                medication_name=data.get('medication_name'),
                presentation=data.get('presentation'),
                dose=data.get('dose'),
                unit=data.get('unit')
            ).exists():
                raise serializers.ValidationError("La combinación de Nombre, Presentación, Dosis y Unidad ya existe.")
        else:
            # Para creaciones
            if MedicationSKU.objects.filter(
                medication_name=data.get('medication_name'),
                presentation=data.get('presentation'),
                dose=data.get('dose'),
                unit=data.get('unit')
            ).exists():
                raise serializers.ValidationError("La combinación de Nombre, Presentación, Dosis y Unidad ya existe.")
        return data
