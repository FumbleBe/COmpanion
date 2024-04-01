from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOrReadOnly
from rules.models import Path
from rules.serializers import PathListSerializer, PathDetailSerializer


class PathViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Path.objects.all().order_by("slug")
    serializer_class = PathListSerializer
    detail_serializer_class = PathDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]
