from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField()
    type = models.CharField(max_length=3)  # usd, eur, etc.
    source = models.CharField(max_length=255)
