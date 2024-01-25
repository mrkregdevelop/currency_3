from django.core.cache import cache
from django.db.models.signals import post_save, post_delete

from currency.constants import LATEST_RATES_CACHE_KEY
from currency.models import Rate


def clear_latest_rates_cache(**kwargs):
    cache.delete(LATEST_RATES_CACHE_KEY)


post_save.connect(clear_latest_rates_cache, sender=Rate)
post_delete.connect(clear_latest_rates_cache, sender=Rate)
