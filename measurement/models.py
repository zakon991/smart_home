from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=256, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['name']

    def __str__(self):
        return '{0}_{1}'.format(self.name, self.description)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)
    sensor = models.ForeignKey(to=Sensor, blank=False, on_delete=models.CASCADE,
                               related_name='measurements')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['created_at']

    def __str__(self):
        return '{0}_{1}_{2}'.format(self.temperature, self.created_at, self.sensor)



