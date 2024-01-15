from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.filters import OrderingFilter
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer
from django_filters.rest_framework import DjangoFilterBackend

from currency.api.paginators import RatePagination
from currency.api.serializers import RateSerializer
from currency.api.throtling import RateThrottle
from currency.filters import RateFilter
from currency.models import Rate


# class RateListAPIView(ListCreateAPIView):
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer  # json -> obj, obj -> json
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
#
#
# class RateDetailsAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all().order_by('-created')
#     serializer_class = RateSerializer
#     renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer  # json -> obj, obj -> json
    # renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = ('buy', 'sell', 'created')
    throttle_classes = (RateThrottle,)
