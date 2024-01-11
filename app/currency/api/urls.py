from django.urls import path

from currency.api.views import RateListAPIView, RateDetailsAPIView

app_name = 'currency_api'

urlpatterns = [
    path('rates/', RateListAPIView.as_view(), name='rate-list'),
    path('rates/<int:pk>/', RateDetailsAPIView.as_view(), name='rate-details')
]
