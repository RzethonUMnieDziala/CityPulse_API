from django.db import models


class Temperature(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    place = models.CharField(max_length = 128)

class Humidity(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    place = models.CharField(max_length = 128)

class Electricity(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    place = models.CharField(max_length = 128)

class Water(models.Model):
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add = True)
    place = models.CharField(max_length = 128)

class Config(models.Model):
    mac = models.CharField(max_length = 256)
    enabled = models.BooleanField()
    name = models.CharField(max_length = 256)
