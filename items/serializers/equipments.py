from rest_framework import serializers
from django.utils.text import slugify

from items.models import Item, Equipment


class EquipmentListSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["name"])
        return super(EquipmentListSerializer, self).create(validated_data)

    class Meta:
        model = Equipment
        fields = ["name", "slug", "actor"]


class EquipmentDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["name"])
        return super(EquipmentDetailSerializer, self).create(validated_data)

    class Meta:
        model = Equipment
        fields = "__all__"
