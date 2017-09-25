from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class PurchaseHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseHistory
        fields = '__all__'