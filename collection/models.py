from django.db import models
from django.contrib.auth.models import User

# Create your models here
class stock(models.Model):
    name = models.CharField("Stock Name", max_length=200)
    unit = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

