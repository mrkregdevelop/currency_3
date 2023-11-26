from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from currency.forms import RateForm
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


def rate_create(request):

    if request.method == 'POST':  # 2 validate data
        form = RateForm(data=request.POST)

        if form.is_valid():
            form.save()  # get validated data, save Rate.objects.create(**validated_data)
            return HttpResponseRedirect('/rate/list/')

    else:  # 1 render form
        form = RateForm()

    context = {
        'form': form
    }

    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    '''
    BAD /rate/update/?id=1
    GOOD /rate/update/1/
    '''
    # try:
    #     rate = Rate.objects.get(id=pk)
    # except Rate.DoesNotExist:
    #     raise Http404('Rate does not exist!')

    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'POST':  # 2 validate data
        form = RateForm(request.POST, instance=rate)

        if form.is_valid():
            form.save()  # get validated data, save Rate.objects.create(**validated_data)
            return HttpResponseRedirect('/rate/list/')

    elif request.method == 'GET':  # 1 render form
        form = RateForm(instance=rate)

    context = {
        'form': form
    }

    return render(request, 'rate_update.html', context)


def rate_delete(request, pk):
    '''
    BAD /rate/update/?id=1
    GOOD /rate/update/1/
    '''

    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'GET':  # 1 render form
        context = {
            'rate': rate
        }
        return render(request, 'rate_delete.html', context)

    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def rate_details(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    context = {
        'rate': rate
    }
    return render(request, 'rate_delete.html', context)


def status_code(request):
    return HttpResponse(
        'Taras Sheketa',
        status=301,
        headers={'Location': '/rate/list/'}
    )


@csrf_exempt
def request_method(request):
    '''
    GET - Client wants to get data from server (retrieve)

    POST - Client wants to push data to server (create)

    PUT - Client wants to update record (update)

    PATCH - Client wants to partially update record (partial update)

    DELETE - Client wants to delete record from server (delete)

    OPTIONS - Client wants to know which request methods are allowed

    HEAD - Client wants to know about response (no body)

    CRUD

    C - POST (create)
    R - GET (read)
    U - PUT/PATCH (update)
    D - DELETE (delete)
    '''

    if request.method == 'GET':
        message = 'Render client form'
    elif request.method == 'POST':
        message = 'Validate form data'

    return HttpResponse(message)


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
