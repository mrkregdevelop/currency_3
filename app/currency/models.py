from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency_type = models.CharField(max_length=3)
    source = models.CharField(max_length=255)

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     if self.created is None:
    #         self.created = timezone.now()
    #     return super().save(....)
