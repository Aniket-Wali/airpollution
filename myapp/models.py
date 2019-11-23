from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class air_quality_cities(models.Model):
    State = models.CharField(max_length=100)
    City = models.CharField(max_length=100, primary_key= True)
    SO2_Annual_average = models.IntegerField()
    Air_quality_of_SO2 = models.CharField(max_length=100)
    NO2_Annual_average = models.IntegerField()
    Air_quality_of_NO2 = models.CharField(max_length=100)
    PM10_Annual_average = models.IntegerField()
    Air_quality_of_PM10 = models.CharField(max_length=100)

    def __str__(self):
        return self.City


class AQI(models.Model):
    City = models.ForeignKey(air_quality_cities, on_delete=models.CASCADE)
    Index = models.IntegerField()

class air_quality_index(models.Model):
    Quality = models.CharField(max_length=20)
    PM10_low = models.IntegerField()
    PM10_high = models.IntegerField()
    PM2_5_low = models.IntegerField()
    PM2_5_high = models.IntegerField()
    NO2_low = models.IntegerField()
    NO2_high = models.IntegerField()
    O3_low = models.IntegerField()
    O3_high = models.IntegerField()
    CO_low = models.IntegerField()
    CO_high = models.IntegerField()

    def __str__(self):
        return self.Quality
