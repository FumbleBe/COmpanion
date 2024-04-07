from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from items.models import Equipment
from items.serializers import EquipmentListSerializer, EquipmentDetailSerializer
from companion.api.permissions import IsDmOrReadOnly


class EquipmentViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentListSerializer
    detail_serializer_class = EquipmentDetailSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # actor_id = self.request.query_params.get("actor_id")
        actor_id = self.kwargs["actor_id"]
        print(actor_id)
        if actor_id is not None:
            if self.request.user.groups.filter(name="DungeonMaster").exists():
                return Equipment.objects.filter(actor__id=actor_id)
            else:
                return Equipment.objects.all()
        else:
            return Equipment.objects.all()

    # def create(self, request, *args, **kwargs):
    #     items = self.request.query_params.get("items")
    #     print(items)
    #     return super().create(request, *args, **kwargs)
