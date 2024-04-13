from rest_framework import serializers
from django.utils.text import slugify

from django.shortcuts import get_object_or_404

from items.models import Inventory, Item
from actors.models import Actor


class InventoryListSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     actor_id = self.context["request"].parser_context["kwargs"]["actor_id"]
    #     actor = Actor.objects.get(id=actor_id)
    #     validated_data["actor"] = actor
    #     return super(EquipmentListSerializer, self).create(validated_data)

    class Meta:
        model = Inventory
        fields = ["name", "slug"]


class ItemChoicesField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        items = Item.objects.all().values_list("id", "name")
        kwargs["choices"] = items
        super(ItemChoicesField, self).__init__(**kwargs)


class InventoryCreateSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(read_only=True)
    # actor = serializers.CharField(write_only=True)
    item = ItemChoicesField(write_only=True)

    # def copy_item_to_inventory(item):
    #     inventory = Inventory()

    #     for field in item._meta.fields:
    #         field_name = field.name
    #         field_value = getattr(item, field_name)
    #         setattr(inventory, field_name, field_value)

    #     inventory.save()

    # def create(self, validated_data):
    #     pass
    #     item_id = validated_data["item"]
    #     item = get_object_or_404(Item, id=item_id)

    #     validated_data["slug"] = slugify(item.name)
    #     actor_id = self.context["request"].parser_context["kwargs"]["actor_id"]
    #     actor = Actor.objects.get(id=actor_id)
    #     validated_data["actor"] = actor

    #     # print(validated_data)

    #     return super(InventoryDetailSerializer, self).create(validated_data)

    class Meta:
        model = Inventory
        fields = ["item"]


class InventoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
