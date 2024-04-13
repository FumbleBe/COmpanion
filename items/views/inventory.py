from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from items.models import Inventory, Item
from actors.models import Actor
from items.serializers import (
    InventoryListSerializer,
    InventoryDetailSerializer,
    InventoryCreateSerializer,
)
from companion.api.permissions import IsDmOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.text import slugify


class InventoryViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerializer
    detail_serializer_class = InventoryDetailSerializer
    creation_serialzier_class = InventoryCreateSerializer

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
            raise

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
        # print(self.request.data)
        # serializer = self.get_serializer(data=request.data)
        # print(serializer)

        item_id = self.request.data["item"]
        item = get_object_or_404(Item, id=item_id)

        actor_id = self.kwargs["actor_id"]
        actor = get_object_or_404(Actor, id=actor_id)

        # validated_data["slug"] = slugify(item.name)
        # actor_id = self.context["request"].parser_context["kwargs"]["actor_id"]
        # actor = Actor.objects.get(id=actor_id)
        # validated_data["actor"] = actor
        self.copy_item_to_inventory(item, actor)
        # for field in item._meta.fields:
        #     field_name = field.name
        #     field_value = getattr(item, field_name)
        #     if field_name != "id":
        #         # setattr(validated_data, field_name, field_value)
        #         validated_data[field_name] = field_value

        # del validated_data['item']

        return super().create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     # items = self.request.query_params.get("items")
    #     actor_id = self.kwargs["actor_id"]
    #     actor = get_object_or_404(Actor, id=actor_id)

    #     return super().create(request, *args, **kwargs)
