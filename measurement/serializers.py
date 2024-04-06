from rest_framework import serializers

from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    """Вывод информации по всем измерениям"""
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class MeasurementEntrySerializer(serializers.ModelSerializer):
    """Вывод информации для ввода измерения"""
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']


class SensorSerializer(serializers.ModelSerializer):
    """Вывод информации по всем датчикам"""
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorEditSerializer(serializers.ModelSerializer):
    """Вывод для изменения информации по датчику"""
    class Meta:
        model = Sensor
        fields = ['description']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Вывод полной информации по конкретному датчику"""
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
