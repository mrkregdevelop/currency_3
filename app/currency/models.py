from django.db import models

from currency.choices import CurrencyTypeChoices


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency_type = models.SmallIntegerField(
        choices=CurrencyTypeChoices.choices,
        # default=1, WRONG
        default=CurrencyTypeChoices.USD  # correct
        # if field contains choices, then human readable format = get_<field_name>_display()
    )
    source = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class Source(models.Model):
    name = models.CharField(max_length=64)
