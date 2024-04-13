from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOrReadOnly
from rules.models import Species
from rules.serializers import SpeciesListSerializer, SpeciesDetailSerializer
from django.utils.text import slugify


class SpeciesViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Species.objects.all().order_by("name")
    serializer_class = SpeciesListSerializer
    detail_serializer_class = SpeciesDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]

    # def create(self, request, *args, **kwargs):
    #     request.data._mutable = True
    #     request.data["slug"] = slugify(request.data["name"])
    #     request.data._mutable = False
    #     return super().create(request, *args, **kwargs)
