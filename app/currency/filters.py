import django_filters

from currency.models import Rate


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'sell': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'currency_type': ['exact']
        }
