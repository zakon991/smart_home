# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer, \
    MeasurementEntrySerializer, SensorEditSerializer


class SensorsView(generics.ListCreateAPIView):
    """Класс вывода информации по датчикам"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request, *args, **kwargs):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            sensor_data = serializer.save()
            serializer = SensorSerializer(sensor_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementView(generics.ListCreateAPIView):
    """Класс вывода информации по измерениям"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, *args, **kwargs):
        serializer = MeasurementEntrySerializer(data=request.data)
        if serializer.is_valid():
            meas_data = serializer.save()
            serializer = MeasurementEntrySerializer(meas_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorIdView(generics.RetrieveUpdateAPIView):
    """Класс изменения информации по датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PATCH not allowed"})
        try:
            instance = Sensor.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = SensorEditSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            sens_data = serializer.save()
            serializer = SensorEditSerializer(sens_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def sensor_id(request, id_sensor):
    return HttpResponse(f'Датчик: {id_sensor}')


def test_view(response):
    return HttpResponse('test')
