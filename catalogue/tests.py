
# Create your tests here.
# catalogue/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MedicationSKU

class MedicationSKUTests(APITestCase):
    def setUp(self):
        self.sku = MedicationSKU.objects.create(
            medication_name="Amoxicillin",
            presentation="Tablet",
            dose=50,
            unit="mg"
        )
        self.list_url = reverse('sku-list')
        self.bulk_create_url = reverse('sku-bulk-create')

    def test_create_sku(self):
        data = {
            "medication_name": "Ibuprofen",
            "presentation": "Capsule",
            "dose": 200,
            "unit": "mg"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MedicationSKU.objects.count(), 2)
        self.assertEqual(MedicationSKU.objects.get(id=response.data['id']).medication_name, "Ibuprofen")

    def test_bulk_create_skus(self):
        data = [
            {
                "medication_name": "Paracetamol",
                "presentation": "Tablet",
                "dose": 500,
                "unit": "mg"
            },
            {
                "medication_name": "Cetirizine",
                "presentation": "Syrup",
                "dose": 10,
                "unit": "ml"
            }
        ]
        response = self.client.post(self.bulk_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MedicationSKU.objects.count(), 3)

    def test_get_sku_list(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_sku(self):
        url = reverse('sku-detail', args=[self.sku.id])
        data = {
            "medication_name": "Amoxicillin",
            "presentation": "Capsule",
            "dose": 100,
            "unit": "mg"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sku.refresh_from_db()
        self.assertEqual(self.sku.presentation, "Capsule")
        self.assertEqual(self.sku.dose, 100)

    def test_delete_sku(self):
        url = reverse('sku-detail', args=[self.sku.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MedicationSKU.objects.count(), 0)

    def test_unique_medication_name(self):
        data = {
            "medication_name": "Amoxicillin",  # Duplicate
            "presentation": "Syrup",
            "dose": 250,
            "unit": "ml"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unique_combination(self):
        data = {
            "medication_name": "Azithromycin",
            "presentation": "Tablet",
            "dose": 50,
            "unit": "mg"  # Same combination as existing SKU
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
