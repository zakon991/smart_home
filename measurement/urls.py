from django.urls import path

from measurement.views import MeasurementView, SensorsView, SensorIdView, sensor_id, test_view

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorIdView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('test/', test_view),
    path('sensor/<int:id_sensor>/', sensor_id),
]