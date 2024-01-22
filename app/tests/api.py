from django.urls import reverse

from currency.models import Source, Rate


def test_get_rate_list(api_client_auth):
    response = api_client_auth.get(reverse('currency_api:rate-list'))
    assert response.status_code == 200
    assert response.json()


def test_post_rate_list_empty_body(api_client_auth):
    response = api_client_auth.post(reverse('currency_api:rate-list'))
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sell': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_post_rate_list_valid_data(api_client_auth):
    initial_count = Rate.objects.count()
    source = Source.objects.create(name='Test', code_name='test')
    payload = {
        'buy': '37.00',
        'sell': '38.00',
        'source': source.id
    }
    response = api_client_auth.post(reverse('currency_api:rate-list'), data=payload)
    assert response.status_code == 201
    assert Rate.objects.count() == initial_count + 1


def test_post_rate_list_invalid_data(api_client_auth):
    source = Source.objects.create(name='Test', code_name='test')
    payload = {
        'buy': '37.000',
        'sell': '38.00',
        'source': source.id,
    }
    response = api_client_auth.post(reverse('currency_api:rate-list'), data=payload)
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['Ensure that there are no more than 2 decimal places.']
    }
