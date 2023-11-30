from import_export import resources

from currency.models import Rate


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate
