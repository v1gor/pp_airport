from rest_framework import serializers
from quickstart.models import Airplane, AirCompany
from math import log


class AirCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = AirCompany
        fields = ['id', 'name', 'exp']



class AirplaneSerializer(serializers.ModelSerializer):
    tank_capacity = serializers.SerializerMethodField()
    fuel_consumption = serializers.SerializerMethodField()
    aircompany  = AirCompanySerializer()

    
    def get_tank_capacity(self, obj):
        return obj.id * 200

    def get_fuel_consumption(self, obj):
        return log(obj.id) * 0.8


    class Meta:
        model = Airplane
        fields = ['id', 'name', 
                  'tank_capacity', 
                  'fuel_consumption',
                  'aircompany']







