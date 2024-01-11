from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from currency.api.serializers import RateSerializer
from currency.models import Rate


class RateListAPIView(ListCreateAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json -> obj, obj -> json


class RateDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
