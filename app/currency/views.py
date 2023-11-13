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

    return HttpResponse(str(results), status=500)


def status_code(request):
    return HttpResponse(
        'Taras Sheketa',
        status=301,
        headers={'Location': '/rate/list/'}
    )


'''
1xx - informational response
2xx - success

200 Ok
201 Created
202 Accepted
204 No Content

3xx - redirection

301 Moved Permanently
302 Found (Previously "Moved temporarily")

4xx - client errors

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed

5xx - server errors

500 Internal Server Error

'''
