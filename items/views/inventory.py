from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from items.models import Inventory, Item
from actors.models import Actor
from items.serializers import (
    InventoryListSerializer,
    InventoryDetailSerializer,
    InventoryCreateSerializer,
)

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.text import slugify


class InventoryViewset(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
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
            raise

    def get_serializer_class(self):
        if self.action == "create":
            return InventoryCreateSerializer
        if self.action == "list":
            return InventoryListSerializer
        if self.action == "retrieve" or "update":
            return InventoryDetailSerializer
        else:
            return InventoryListSerializer

    def copy_item_to_inventory(self, item, actor):
        inventory = Inventory()

        for field in item._meta.fields:
            field_name = field.name
            field_value = getattr(item, field_name)
            if field_name != "id":
                setattr(inventory, field_name, field_value)

        inventory.slug = slugify(item.name)
        inventory.actor = actor
        inventory.save()

    def create(self, request, *args, **kwargs):
        item_id = self.request.data["item"]
        item = get_object_or_404(Item, id=item_id)

        actor_id = self.kwargs["actor_id"]
        actor = get_object_or_404(Actor, id=actor_id)

        self.copy_item_to_inventory(item, actor)
        
        # return super().create(request, *args, **kwargs)
        return Response(
            status=201
        )
