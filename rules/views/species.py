from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOrReadOnly
from rules.models import Species
from rules.serializers import SpeciesListSerializer, SpeciesDetailSerializer


class SpeciesViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Species.objects.all().order_by("name")
    serializer_class = SpeciesListSerializer
    detail_serializer_class = SpeciesDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]
