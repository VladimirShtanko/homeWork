from rest_framework import serializers

from .models import Car
from accounts.models import Users

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'username',
            'first_name',
            'last_name',
            'role',
        ]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'factory_number',
            'car_model',
            'dvig_model',
            'dvig_number',
            'transmission_model',
            'transmission_number',
            'main_bridge_model',
            'main_bridge_number',
            'controlled_bridge_model',
            'controlled_bridge_number',
            'contract',
            'date',
            'consignee',
            'address',
            'complete_set',
            'client',
            'company',
        ]
        depth = 1