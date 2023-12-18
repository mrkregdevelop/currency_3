from django.db import models
from django.utils.translation import gettext_lazy as _

from currency.choices import CurrencyTypeChoices


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency_type = models.SmallIntegerField(
        _('Currency type'),
        choices=CurrencyTypeChoices.choices,
        # default=1, WRONG
        default=CurrencyTypeChoices.USD  # correct
        # if field contains choices, then human-readable format = get_<field_name>_display()
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class Source(models.Model):
    '''
    One To One - X
    One To Many - V
    Many To Many - ~


    rate_set
    '''
    name = models.CharField(_('Source'), max_length=64)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    name = models.CharField(_('Name'), max_length=64)
    email = models.EmailField(_('Email'), max_length=128)
    subject = models.CharField(_('Subject'), max_length=256)
    body = models.CharField(_('Body'), max_length=2048)

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')
