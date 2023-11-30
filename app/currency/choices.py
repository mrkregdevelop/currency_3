from django.db import models

# CURRENCY_USD = 1
# CURRENCY_EUR = 2
#
# CURRENCY_TYPE = (
#     (CURRENCY_USD, 'Dollar'),
#     (CURRENCY_EUR, 'Euro'),
# )


class CurrencyTypeChoices(models.IntegerChoices):
    USD = 2, 'Dollar'
    EUR = 1, 'Euro'
