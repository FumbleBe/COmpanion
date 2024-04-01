from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOrReadOnly
from rules.models import Capacity
from rules.serializers import CapacityListSerializer, CapacityDetailSerializer


class CapacityViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Capacity.objects.all().order_by("slug")
    serializer_class = CapacityListSerializer
    detail_serializer_class = CapacityDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]
