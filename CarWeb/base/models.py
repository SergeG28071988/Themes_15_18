from django.db import models

class Auto(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

