from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from items.models import Item
from items.serializers import ItemListSerializer, ItemDetailSerializer
from companion.api.permissions import IsDmOrReadOnly


class ItemViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    detail_serializer_class = ItemDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]

    def get_queryset(self):
        if self.request.user.groups.filter(name="DungeonMaster").exists():
            return Item.objects.all()
        else:
            return Item.objects.filter(
                access__in=[self.request.user]
            ) | Item.objects.filter(access__isnull=True)
