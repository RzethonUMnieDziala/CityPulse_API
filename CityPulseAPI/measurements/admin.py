from django.contrib import admin
from measurements.models import Temperature, Humidity, Electricity, Water, Pollution, Config
# Register your models here.

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Electricity)
admin.site.register(Water)
admin.site.register(Pollution)
admin.site.register(Config)
