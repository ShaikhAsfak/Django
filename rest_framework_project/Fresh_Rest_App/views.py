from django.shortcuts import render
from rest_framework import viewsets , permissions
from .models import RestProductModel
from .serializers import RestProductSerializer

# Create your views here.

class RestProductViewSet(viewsets.ModelViewSet):
    queryset = RestProductModel.objects.all()
    serializer_class = RestProductSerializer
    permission_classes = [permissions.IsAuthenticated]