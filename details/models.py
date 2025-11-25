from django.db import models


class CityWeather(models.Model):
    name = models.CharField(max_length=55)
    country = models.CharField(max_length=5)
    temp = models.IntegerField()
    wind = models.DecimalField(max_digits=10, decimal_places=4)
    weather = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.id)

