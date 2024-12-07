from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer

# Create your views here.
class MedicationSKUViewSet(viewsets.ModelViewSet):
    queryset = MedicationSKU.objects.all()
    serializer_class = MedicationSKUSerializer

    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        serializer = MedicationSKUSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
