from rest_framework import serializers
from django.utils.text import slugify

from items.models import Equipment, Item
from actors.models import Actor


class EquipmentListSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     actor_id = self.context["request"].parser_context["kwargs"]["actor_id"]
    #     actor = Actor.objects.get(id=actor_id)
    #     validated_data["actor"] = actor
    #     return super(EquipmentListSerializer, self).create(validated_data)

    class Meta:
        model = Equipment
        fields = ["name", "slug"]


class MultipleChoicesField(serializers.MultipleChoiceField):
    def __init__(self, **kwargs):
        items = Item.objects.all().values_list("id", "name")
        kwargs["choices"] = items
        super(MultipleChoicesField, self).__init__(**kwargs)


class EquipmentDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    actor = serializers.CharField(read_only=True)
    items = MultipleChoicesField()

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["name"])
        actor_id = self.context["request"].parser_context["kwargs"]["actor_id"]
        actor = Actor.objects.get(id=actor_id)
        validated_data["actor"] = actor
        return super(EquipmentListSerializer, self).create(validated_data)

    class Meta:
        model = Equipment
        fields = ['slug', 'actor', 'items']
