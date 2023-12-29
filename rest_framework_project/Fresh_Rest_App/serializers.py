
from rest_framework import serializers
from .models import RestProductModel



class RestProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestProductModel
        fields = '__all__'