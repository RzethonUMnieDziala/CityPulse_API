from measurements.models import Temperature, Humidity, Electricity, Water, Config
from rest_framework import serializers

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ('value', 'date', 'place')

class HumiditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Humidity
        fields = ('value', 'date', 'place')

class ElectricitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Electricity
        fields = ('value', 'date', 'place')

class WaterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Water
        fields = ('value', 'date', 'place')

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ('value', 'date', 'place')
