from measurements.models import Temperature, Humidity, Electricity, Water, Pollution, Config
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

class PollutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pollution
        fields = ('value', 'date', 'place')

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = ('mac', 'enabled', 'name')
