from django.http.response import HttpResponse
from django.shortcuts import render

from currency.models import Rate


def rate_list(request):
    '''
    MVT(MVC) U
    M - model
    V - view
    T - template
    U - urls
    '''
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'rate_list.html', context)


def status_code(request):
    return HttpResponse(
        'Taras Sheketa',
        status=301,
        headers={'Location': '/rate/list/'}
    )


def test_template(request):
    name = request.GET.get('name')
    context = {
        'username': name
    }

    return render(request, 'test.html', context)


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
