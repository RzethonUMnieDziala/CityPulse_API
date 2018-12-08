from measurements.api.viewsets import TemperatureViewSet, HumidityViewSet, ElectricityViewSet, WaterViewSet, PollutionViewSet, ConfigViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('temperature', TemperatureViewSet, base_name='temperature')
router.register('humidity', HumidityViewSet, base_name='humidity')
router.register('electricity', ElectricityViewSet, base_name='electricity')
router.register('water', WaterViewSet, base_name='water')
router.register('pollution', PollutionViewSet, base_name='pollution')
router.register('config', ConfigViewSet, base_name='config')
