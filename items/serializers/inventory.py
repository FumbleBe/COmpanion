from rest_framework import serializers
from items.models import Inventory, Item


class InventoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ["id", "name", "slug"]


class ItemChoicesField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        items = Item.objects.all().values_list("id", "name")
        kwargs["choices"] = items
        super(ItemChoicesField, self).__init__(**kwargs)


class InventoryCreateSerializer(serializers.ModelSerializer):
    item = ItemChoicesField()

    class Meta:
        model = Inventory
        fields = ["item"]


class InventoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = "__all__"
