from time import time

from django.core.mail import send_mail
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy


from currency.forms import RateForm
from currency.models import Rate, ContactUs


class RateListView(ListView):
    queryset = Rate.objects.all()
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

        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

        return redirect
