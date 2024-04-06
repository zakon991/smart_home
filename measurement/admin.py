from django.contrib import admin

from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'created_at', 'sensor')
    list_filter = ('id', 'sensor')
    search_fields = ('id', 'sensor')
