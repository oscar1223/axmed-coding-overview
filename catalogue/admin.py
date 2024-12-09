from django.contrib import admin
from .models import MedicationSKU

# Register your models here.

@admin.register(MedicationSKU)
class MedicationSKUAdmin(admin.ModelAdmin):
    list_display = ('medication_name', 'presentation', 'dose', 'unit')
    search_fields = ('medication_name',)


