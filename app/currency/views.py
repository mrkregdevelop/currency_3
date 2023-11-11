from django.http.response import HttpResponse

from currency.models import Rate


def rate_list(request):

    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, type: {rate.type}, '
            f'source: {rate.source}, created: {rate.created} <br>'
        )

    return HttpResponse(str(results))
