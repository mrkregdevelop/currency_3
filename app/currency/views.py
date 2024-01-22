import re
import json
from datetime import datetime, timedelta
from time import time

from django.views.generic import (
    CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)
from django_filters.views import FilterView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.response import Response

from currency.filters import RateFilter
from currency.forms import RateForm
from currency.models import Rate, ContactUs
from currency.tasks import send_email_in_background


class RateListView(FilterView):
    queryset = Rate.objects.all().select_related('source').order_by('-created')
    template_name = 'rate_list.html'
    paginate_by = 30
    filterset_class = RateFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        query_parameters = self.request.GET.urlencode()
        # context['filter_params'] = '&'.join(
        #     f'{key}={value}' for key, value in self.request.GET.items()
        #     if key != 'page'
        # )

        context['filter_params'] = re.sub(r'page=\d+', '', query_parameters).lstrip('&')

        return context


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_detail.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'name',
        'email',
        'subject',
        'body',
    )

    def _send_email(self):
        '''
        | 00:00 - 07:59 | 08:00 - 17:59 | 18:00 - 23:59 |
        | eta - 8:00    |  now          | eta - 8:00 next day|
        '''
        # recipient = 'hileltest1234@gmail.com'
        # WRONG! from settings import settings
        from django.conf import settings
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
                Name: {self.object.name}
                Email: {self.object.email}
                Subject: {self.object.subject}
                Body: {self.object.body}
                '''
        eta = datetime.now() + timedelta(seconds=60)
        send_email_in_background.apply_async(
            kwargs={
                'subject': subject,
                'body': body
            }
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

        return redirect
