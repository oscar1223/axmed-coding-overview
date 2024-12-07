from django.db import models

# Create your models here.

class MedicationSKU(models.Model):
    medication_name = models.CharField(max_length=225, unique=True)
    presentation = models.CharField(max_length=225)
    dose = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)

    class Meta:
        unique_together = ('presentation', 'dose', 'unit')

    def __str__(self):
        return f"{self-medication_name} - {self.presentation} - {self.dose} - {self.unit}"

        