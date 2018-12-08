from rest_framework import viewsets
from measurements.models import Temperature, Humidity, Electricity, Water, Config
from .serializers import TemperatureSerializer, HumiditySerializer, ElectricitySerializer, WaterSerializer, ConfigSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters

class TemperatureFilter(filters.FilterSet):
    class Meta:
        model = Temperature
        fields =    {
            'value' :['iexact','lte','gte'],
            'place': ['icontains'],
            'date' : ['iexact','lte','gte'],
        }

class HumidityFilter(filters.FilterSet):
    class Meta:
        model = Humidity
        fields = {
            'value' :['iexact','lte','gte'],
            'place': ['icontains'],
            'date' : ['iexact','lte','gte'],
        }

class ElectricityFilter(filters.FilterSet):
    class Meta:
        model = Electricity
        fields = {
            'value' :['iexact','lte','gte'],
            'place': ['icontains'],
            'date' : ['iexact','lte','gte'],
        }

class WaterFilter(filters.FilterSet):
    class Meta:
        model = Water
        fields = {
            'value' :['iexact','lte','gte'],
            'place': ['icontains'],
            'date' : ['iexact','lte','gte'],
        }

class ConfigFilter(filters.FilterSet):
    class Meta:
        model = Config
        fields = {
            'mac' : ['iexact'],
            'enabled' : ['iexact'],
            #possible change to icontains
            'name' : ['iexact'],
        }

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    filterset_class = TemperatureFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class HumidityViewSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all()
    serializer_class = HumiditySerializer
    filterset_class = HumidityFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class ElectricityViewSet(viewsets.ModelViewSet):
    queryset = Electricity.objects.all()
    serializer_class = ElectricitySerializer
    filterset_class = ElectricityFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class WaterViewSet(viewsets.ModelViewSet):
    queryset = Water.objects.all()
    serializer_class = WaterSerializer
    filterset_class = WaterFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
    filterset_class = ConfigFilter
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
