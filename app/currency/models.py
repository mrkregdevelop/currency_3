from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField()
    currency_type = models.CharField(max_length = 3)
    source = models.CharField(max_length=255)
