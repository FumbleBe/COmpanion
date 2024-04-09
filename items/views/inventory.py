from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from items.models import Inventory
from actors.models import Actor
from items.serializers import InventoryListSerializer, InventoryDetailSerializer
from companion.api.permissions import IsDmOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import Http404


class InventoryViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerializer
    detail_serializer_class = InventoryDetailSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # actor_id = self.request.query_params.get("actor_id")
        actor_id = self.kwargs["actor_id"]
        actor = get_object_or_404(Actor, id=actor_id)
        if actor_id is not None:
            if self.request.user.groups.filter(name="DungeonMaster").exists():
                return Inventory.objects.filter(actor=actor)
            try: 
                if self.request.user == actor.owner:
                    return Inventory.objects.filter(actor=actor)
                else:
                    raise Http404
            except AttributeError:
                raise Http404
        else:
            raise Http404

    # def create(self, request, *args, **kwargs):
    #     # items = self.request.query_params.get("items")
    #     actor_id = self.kwargs["actor_id"]
    #     actor = get_object_or_404(Actor, id=actor_id)


    #     return super().create(request, *args, **kwargs)
