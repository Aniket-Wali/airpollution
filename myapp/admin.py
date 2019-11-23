from django.contrib import admin
from myapp.models import air_quality_cities,air_quality_index, AQI
# Register your models here.

admin.site.register(air_quality_cities)
admin.site.register(air_quality_index)
admin.site.register(AQI)
