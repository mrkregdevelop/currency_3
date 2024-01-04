from datetime import datetime, timedelta
from time import time

from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy


from currency.forms import RateForm
from currency.models import Rate, ContactUs
from currency.tasks import send_email_in_background


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'rate_list.html'


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


class TimeItMixin:

    def dispatch(self, request, *args, **kwargs):
        print('BEFORE IN VIEW')
        start = time()

        response = super().dispatch(request, *args, **kwargs)

        end = time()
        print(f'AFTER IN VIEW {end - start}')

        return response


class ContactUsCreateView(TimeItMixin, CreateView):
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
